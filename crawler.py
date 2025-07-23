import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited = set()

def crawl_site(base_url, max_depth=2, session=None):
    if not session:
        session = requests.Session()
    urls = set()
    forms = []
    def crawl(url, depth):
        if depth > max_depth or url in visited:
            return
        visited.add(url)
        try:
            res = session.get(url, timeout=5)
            soup = BeautifulSoup(res.text, "html.parser")
            for form in soup.find_all("form"):
                forms.append((url, str(form)))
            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link["href"])
                if urlparse(full_url).netloc == urlparse(base_url).netloc:
                    urls.add(full_url)
                    crawl(full_url, depth + 1)
        except:
            pass
    crawl(base_url, 0)
    return list(urls), forms
