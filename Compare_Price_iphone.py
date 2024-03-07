from bs4 import BeautifulSoup
from selenium import webdriver


def get_product_price_xcite(product_name):
    url = product_name
    driver = webdriver.Chrome()
    driver.get(url)  
    soup = BeautifulSoup(driver.page_source, 'html.parser') 
    price_element = soup.find("span", class_="text-3xl text-functional-red-800")
    driver.quit()
    if price_element:
        return price_element.text.strip()
    else:
        return "Price not found on Xcite"
    
def get_product_price_Blink(product_name):
    url = product_name
    driver = webdriver.Chrome()
    driver.get(url)  
    soup = BeautifulSoup(driver.page_source, 'html.parser') 
    price_element = soup.find("span", attrs={'id':"currentProductPrice",'class':"product-price text-sky"})
    if price_element:
        return price_element.text.strip()
    else:
        return "Price not found on Blink"
    
def get_product_price_Best(product_name):
    url = product_name
    driver = webdriver.Chrome()
    driver.get(url)  
    soup = BeautifulSoup(driver.page_source, 'html.parser') 
    price_element = soup.find("div", class_="product-price")
    if price_element:
        return price_element.text.strip()
    else:
        return "Price not found on Best"
    
def get_product_eureka_price(product_name):
    url = product_name
    driver = webdriver.Chrome()
    driver.get(url)  
    soup = BeautifulSoup(driver.page_source, 'html.parser') 
    price_element = soup.find("span", class_="amount")
    if price_element:
        return price_element.text.strip()
    else:
        return "Price not found on eureka"
    
product_url_Xcite= "https://www.xcite.com/apple-iphone-15-pro-max-6-7-inch-256gb-8gb-ram-5g-natural/p"
product_url_eureka= "https://www.eureka.com.kw/products/details/235203"
product_url_Blink="https://www.blink.com.kw/en/Apple-iPhone-15-Pro-Max-5G--256GB--Natural-Titanium"
product_url_Best="https://best.com.kw/en/product/IPH-15PM-256-TN-ES/Apple-iPhone-15-Pro-Max-256GB---Natural-Titanium--One-Physical-nano-SIM---One-eSIM-"
Xcite_price = get_product_price_xcite(product_url_Xcite)
Blink_price = get_product_price_Blink(product_url_Blink)
Best_price = get_product_price_Best(product_url_Best)
eureka_price = get_product_eureka_price(product_url_eureka)



print(f"iphone 15pro max price on Xcite: {Xcite_price}")
print(f"iphone 15pro max price on Blink: {Blink_price}")
print(f"iphone 15pro max price on Best: {Best_price}")
print(f"iphone 15pro max price on eureka: {eureka_price}")




