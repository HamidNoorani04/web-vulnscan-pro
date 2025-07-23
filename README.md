# Web VulnScan Pro
# -Abdul Hamid Noorani
A Python-based web vulnerability scanner that crawls a target website and detects common vulnerabilities like XSS and SQL Injection.

## Features

- Crawl internal links up to depth 2
- Parse and analyze forms and URL parameters
- Detect:
  - Cross-Site Scripting (XSS)
  - SQL Injection (SQLi)
- Output a detailed JSON report
- Clean and modular Python code

## Usage

```bash
python3 scanner.py https://example.com -o scan_report.json
```

## Requirements

- Python 3.x
- requests
- beautifulsoup4

Install dependencies:

```bash
pip install -r requirements.txt
```

## Sample Output

```json
{
    "vulnerabilities": [
        {
            "url": "https://example.com/search",
            "type": "XSS",
            "payload": "<script>alert(1)</script>"
        }
    ]
}
```

## Disclaimer

For educational and authorized testing purposes only.
