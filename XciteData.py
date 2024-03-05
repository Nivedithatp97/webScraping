from bs4 import BeautifulSoup
import openpyxl

with open("Xcite.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

list_items = soup.find_all("li", class_="col-span-2 sm:col-span-4 sp:col-span-3 md:col-span-4 lg:col-span-3 xl:col-span-2 relative flex text-center")
wb = openpyxl.Workbook()
sheet = wb.active

sheet["A1"] = "Product Name"
sheet["B1"] = "Product Price"
sheet.column_dimensions['A'].width = 60  
sheet.column_dimensions['B'].width = 30

row = 2

for item in list_items:
    product_name_elem = item.find("p", class_="mb-2 typography-default ProductTile_productName__R9tA5")
    product_name = product_name_elem.text.strip() if product_name_elem else " "
    
    product_price_elem = item.find("span", class_="text-2xl text-functional-red-800 block mb-2")
    product_price = product_price_elem.text.strip() if product_price_elem else " "

    sheet[f"A{row}"] = product_name
    sheet[f"B{row}"] = product_price

    row += 1
wb.save("Xcite_products.xlsx")
