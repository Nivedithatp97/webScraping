from bs4 import BeautifulSoup
import openpyxl

with open("best.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

list_items = soup.find_all("best-product-grid-item", class_="col-lg-3 col-md-4 col-sm-6 ng-star-inserted")
wb = openpyxl.Workbook()
sheet = wb.active

sheet["A1"] = "Product Name"
sheet["B1"] = "Product Price"
sheet.column_dimensions['A'].width = 60  
sheet.column_dimensions['B'].width = 30

row = 2

for item in list_items:
    product_name_elem = item.find("a", class_="cx-product-name")
    product_name = product_name_elem.text.strip() if product_name_elem else " "
    
    for span in item.find_all("span", class_="depricated-price ng-star-inserted"):
        span.decompose()
    product_price_elem = item.find("div", class_="cx-product-price")
    product_price = product_price_elem.text.strip() if product_price_elem else " "
    

    sheet[f"A{row}"] = product_name
    sheet[f"B{row}"] = product_price

    row += 1
wb.save("best_mobile_products.xlsx")
