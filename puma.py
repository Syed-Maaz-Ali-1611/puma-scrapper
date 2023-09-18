from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from csv import writer
import time


# opening drivers and url
url = "https://us.puma.com/us/en"
driver = Service("E:\learning\python\webscrapping\chromedriver.exe")
browser = webdriver.Chrome(service=driver)
browser.get(url)
browser.maximize_window()

#title of the web 
my_title = browser.title
print(my_title)

# find the search box element and enter a search term
search_box = browser.find_element(By.CLASS_NAME, "border-white")
search_box.send_keys("shoes")
search_box.send_keys(Keys.ENTER)

# wait for the search results to load
time.sleep(5)

soup = BeautifulSoup(browser.page_source, "html.parser")

# find all the products on the page
products = soup.find_all("li", {"data-test-id": "product-list-item"})

# iterate over the products and extract the information we want
filename = input("Enter file name : ")
with open(f'{filename}.csv', 'w', encoding='utf8', newline='')as f:
    thewriter = writer(f)
    header = ["Name", "Price", "Image_url"]
    thewriter.writerow(header)
    for product in products:
        name = product.find("span", {"class" :  "sr-only"}).text.strip()
        price = product.find("span", {"data-test-id": "price"}).text.strip()
        image_url = product.find("img", {"class" :  "w-full"})["src"]
        print("Name : ", name)
        print("Price : ", price)
        print("Image_url : ", image_url)
        print("\n")
        info = [name, price, image_url]
        thewriter.writerow(info)
        

# # # close the browser

time.sleep(30)