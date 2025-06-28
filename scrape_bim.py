import requests
from parse_pdf import extract_products

def scrape_bim():
    pdf_url = "https://www.bim.com.tr/m/pdf/aktuel.pdf"
    resp = requests.get(pdf_url, headers={"User-Agent":"Mozilla/5.0"})
    resp.raise_for_status()
    with open("bim.pdf", "wb") as f:
        f.write(resp.content)

    items = extract_products("bim.pdf")
    return {"site": "BİM", "items": items}
