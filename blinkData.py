from bs4 import BeautifulSoup
import openpyxl
from selenium import webdriver

url="https://www.blink.com.kw/en/Product/Products?searchText=mobile%20phone&sortBy=&filterBy=cat:"
driver=webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")

list_items = soup.find_all("div", class_="items")
wb = openpyxl.Workbook()
sheet = wb.active

sheet["A1"] = "Product Name"
sheet["B1"] = "Product Price"
sheet.column_dimensions['A'].width = 60  
sheet.column_dimensions['B'].width = 30

row = 2

for item in list_items:
    product_name_elem = item.find("span", class_="item_name noSwipe")
    product_name = product_name_elem.text.strip() if product_name_elem else " "
    
    product_price_elem = item.find("span", class_="newprice alignright bluetext noSwipe")
    product_price = product_price_elem.text.strip() if product_price_elem else " "

    sheet[f"A{row}"] = product_name
    sheet[f"B{row}"] = product_price

    row += 1
wb.save("Blink_mobile_products.xlsx")
