# scrape_a101.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from parse_pdf import extract_products

def scrape_a101():
    base = "https://www.a101.com.tr"
    r = requests.get(base, headers={"User-Agent":"Mozilla/5.0"})
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    obj = soup.find("object",{"type":"application/pdf"})
    pdf_url = urljoin(base, obj["data"])
    resp = requests.get(pdf_url); open("a101.pdf","wb").write(resp.content)
    items = extract_products("a101.pdf")
    return {"site":"A101", "items": items}