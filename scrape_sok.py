# scrape_sok.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from parse_pdf import extract_products

def scrape_sok():
    base = "https://www.sokmarket.com.tr/?srsltid=AfmBOoomDLEnKEYHc_pDzauQ2Pw_tvFfuj92veRpHkqZ1emgo2VNVKxY"
    r = requests.get(base, headers={"User-Agent":"Mozilla/5.0"})
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    obj = soup.find("object",{"type":"application/pdf"})
    pdf_url = urljoin(base, obj["data"])
    resp = requests.get(pdf_url); open("sok.pdf","wb").write(resp.content)
    items = extract_products("sok.pdf")
    return {"site":"sok", "items": items}