# Web VulnScan Pro (Final Version)
## 👤 Built With Pride By

**Hamid Noorani**  
📧 hamidnoorani04@gmail.com 
🔗 [GitHub](https://github.com/HamidNoorani04)
🔗 [LinkedIn](https://linkedin.com/in/abdul-hamid-noorani-37258a351)


A professional Python tool for scanning web applications for common vulnerabilities.

## 🔐 Features
- XSS, SQL Injection, LFI, Open Redirects
- POST-based form injection
- Login with session authentication
- Clean JSON reports

## 🔧 Requirements

```bash
pip install requests beautifulsoup4
```

## 🚀 Usage

```bash
python scanner.py https://target.com -o report.json
```

With login:

```bash
python scanner.py https://target.com --login-url https://target.com/login --username admin --password admin123 -o secure-report.json
```

## ⚠️ Legal Disclaimer
Use only on systems you own or have permission to test.
