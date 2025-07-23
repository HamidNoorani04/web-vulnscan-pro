import argparse
from crawler import crawl_site
from analyzer import analyze_urls
from utils import save_report

def main():
    parser = argparse.ArgumentParser(description="Web VulnScan Pro - Advanced Web Vulnerability Scanner")
    parser.add_argument("url", help="Target URL to scan")
    parser.add_argument("-o", "--output", help="Output JSON report file", default="report.json")
    args = parser.parse_args()

    print(f"[+] Starting crawl on: {args.url}")
    urls, forms = crawl_site(args.url)
    print(f"[+] Found {len(urls)} URLs and {len(forms)} forms")

    print("[+] Starting vulnerability analysis...")
    results = analyze_urls(urls, forms)

    save_report(results, args.output)
    print(f"[+] Scan complete. Report saved to {args.output}")

if __name__ == "__main__":
    main()