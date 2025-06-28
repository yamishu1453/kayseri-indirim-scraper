import pdfplumber

def extract_products(path):
    items=[]
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            tbl = page.extract_table()
            if tbl:
                for row in tbl[1:]:
                    items.append({"name":row[0],"price":row[1]})
            else:
                lines = page.extract_text().split("\n")
                for i in range(0,len(lines)-1,2):
                    items.append({"name":lines[i],"price":lines[i+1]})
    return items