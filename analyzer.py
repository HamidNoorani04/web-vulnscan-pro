import requests
from urllib.parse import urlparse, urlencode
import json

with open("payloads.json", "r") as f:
    PAYLOADS = json.load(f)

def analyze_urls(urls, forms):
    report = {"vulnerabilities": []}
    for url in urls:
        for payload in PAYLOADS["xss"]:
            if payload in requests.get(url + "?" + urlencode({"q": payload})).text:
                report["vulnerabilities"].append({
                    "url": url,
                    "type": "XSS",
                    "payload": payload
                })
        for payload in PAYLOADS["sqli"]:
            if "sql" in requests.get(url + "?" + urlencode({"id": payload})).text.lower():
                report["vulnerabilities"].append({
                    "url": url,
                    "type": "SQL Injection",
                    "payload": payload
                })
    return report