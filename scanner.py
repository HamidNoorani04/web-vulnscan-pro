"""
Web VulnScan Pro
Developed by Hamid Noorani 🛡️
A Python-based web vulnerability scanner for ethical hacking and portfolio use.
"""

import argparse
from crawler import crawl_site
from analyzer import analyze_urls
from utils import save_report, login_session

def main():
    parser = argparse.ArgumentParser(description="Web VulnScan Pro - Final Version")
    parser.add_argument("url", help="Target URL to scan")
    parser.add_argument("-o", "--output", help="Output JSON report file", default="report.json")
    parser.add_argument("--login-url", help="Login URL")
    parser.add_argument("--username", help="Username for login")
    parser.add_argument("--password", help="Password for login")
    args = parser.parse_args()

    if args.login_url and args.username and args.password:
        print(f"[+] Logging in as {args.username}...")
        session = login_session(args.login_url, args.username, args.password)
    else:
        import requests
        session = requests.Session()

    print(f"[+] Crawling: {args.url}")
    urls, forms = crawl_site(args.url, session=session)
    print(f"[+] Found {len(urls)} URLs and {len(forms)} forms")

    print("[+] Analyzing for vulnerabilities...")
    report = analyze_urls(urls, forms, session)
    save_report(report, args.output)
    print(f"[+] Scan complete. Report saved to {args.output}")
    report.append({
        "info": "Scan completed using Web VulnScan Pro by Hamid Noorani"}) 

if __name__ == "__main__":
    main()
