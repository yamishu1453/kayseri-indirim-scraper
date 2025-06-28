# run.py
from scrape_a101 import scrape_a101
from scrape_bim import scrape_bim
from scrape_sok import scrape_sok
import json

def main():
    sonuçlar=[]
    for fn in (scrape_a101, scrape_bim, scrape_sok):
        try:
            sonuçlar.append(fn())
        except Exception as e:
            sonuçlar.append({"site":fn.__name__,"error":str(e)})
    with open("aktuel.json","w",encoding="utf-8") as f:
        json.dump(sonuçlar, f, ensure_ascii=False, indent=2)
    print("✅ aktuel.json oluşturuldu")

if __name__=="__main__":
    main()