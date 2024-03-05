from bs4 import BeautifulSoup
import openpyxl

with open("eureka.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

list_items = soup.find_all("li", class_="ais-Hits-item")
print(soup)
wb = openpyxl.Workbook()
sheet = wb.active

sheet["A1"] = "Product Name"
sheet["B1"] = "Product Price"

row = 2

for item in list_items:
    product_name_elem = item.find("span", class_="display-block fwbold")
    product_name = product_name_elem.text.strip() if product_name_elem else " "
    
    product_price_elem = item.find("p", class_="mb5 borred").find('span',attrs={'style':'color:red'})
    product_price = product_price_elem.text.strip() if product_price_elem else " "

    sheet[f"A{row}"] = product_name
    sheet[f"B{row}"] = product_price

    row += 1
wb.save("eureka_products.xlsx")
