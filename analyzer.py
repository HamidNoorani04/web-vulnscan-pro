import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlencode, urlparse
import json

with open("payloads.json") as f:
    PAYLOADS = json.load(f)

def analyze_urls(urls, forms, session):
    report = {"vulnerabilities": []}
    for url in urls:
        for payload in PAYLOADS["xss"]:
            test_url = f"{url}?q={payload}"
            try:
                res = session.get(test_url, timeout=5)
                if payload in res.text:
                    report["vulnerabilities"].append({
                        "url": test_url, "type": "XSS", "payload": payload, "method": "GET"
                    })
            except:
                continue

        for payload in PAYLOADS["sqli"]:
            test_url = f"{url}?id={payload}"
            try:
                res = session.get(test_url, timeout=5)
                if "sql" in res.text.lower() or "syntax" in res.text.lower():
                    report["vulnerabilities"].append({
                        "url": test_url, "type": "SQL Injection", "payload": payload, "method": "GET"
                    })
            except:
                continue

        for payload in PAYLOADS["lfi"]:
            test_url = f"{url}?file={payload}"
            try:
                res = session.get(test_url, timeout=5)
                if "root:x" in res.text or "boot:" in res.text:
                    report["vulnerabilities"].append({
                        "url": test_url, "type": "LFI", "payload": payload, "method": "GET"
                    })
            except:
                continue

        for payload in PAYLOADS["redirect"]:
            test_url = f"{url}?next={payload}"
            try:
                res = session.get(test_url, allow_redirects=False, timeout=5)
                if res.status_code in [301, 302] and payload in res.headers.get("Location", ""):
                    report["vulnerabilities"].append({
                        "url": test_url, "type": "Open Redirect", "payload": payload, "method": "GET"
                    })
            except:
                continue

    for form_url, form_html in forms:
        for payload in PAYLOADS["xss"] + PAYLOADS["sqli"]:
            try:
                res = session.post(form_url, data={"input": payload}, timeout=5)
                if payload in res.text or "sql" in res.text.lower():
                    report["vulnerabilities"].append({
                        "url": form_url, "type": "Form Injection", "payload": payload, "method": "POST"
                    })
            except:
                continue

    return report
