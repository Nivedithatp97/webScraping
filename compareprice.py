from bs4 import BeautifulSoup
from selenium import webdriver

chrome_driver = r'C:\Users\user\Downloads\chrome\chromedriver-win64'

def get_product_price_xcite(product_name):
    url = product_name
    driver = webdriver.Chrome(chrome_driver)
    driver.get(url) 
    soup = BeautifulSoup(driver.page_source, 'html.parser') 
    price_element = soup.find("span", class_="text-2xl text-functional-red-800 block mb-2")
    driver.quit()
    if price_element:
        return price_element.text.strip()
    else:
        return "Price not found on Xcite"
    
def get_product_price_Blink(product_name):
    url = product_name
    driver = webdriver.Chrome(chrome_driver)
    driver.get(url)  
    soup = BeautifulSoup(driver.page_source, 'html.parser') 
    price_element = soup.find("span", class_="newprice alignright bluetext noSwipe")
    driver.quit()
    if price_element:
        return price_element.text.strip()
    else:
        return "Price not found on Blink"

product_url_Xcite= "https://www.xcite.com/search?q=HONOR%20Magic%20V2%207.92-inch%2C%2016GB%20RAM%2C%20512GB%2C%205G%20Phone%2C%20Purple"
product_url_Blink="https://www.blink.com.kw/en/Product/Products?searchText=HONOR%20Magic%20V2%207.92-inch,%2016GB%20RAM,%20512GB,%205G%20Phone,%20Purple&sortBy=&filterBy=cat:"
Xcite_price = get_product_price_xcite(product_url_Xcite)
Blink_price = get_product_price_Blink(product_url_Blink)

print(f"Xcite price: {Xcite_price}")
print(f"Blink price: {Blink_price}")


