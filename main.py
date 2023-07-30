import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By
import lxml
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=True")
chrome_options.add_experimental_option("detach", True)
chrome_web_driver = Service(r"C:\Users\danie\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_web_driver, options=chrome_options)
driver.maximize_window()

RIGHT_MOV_MARKETINFO = "https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E689&minBedrooms=3&propertyTypes=detached%2Csemi-detached%2Cterraced&maxDaysSinceAdded=1&includeSSTC=false&mustHave=garden%2Cparking&dontShow=retirement%2CsharedOwnership&furnishTypes=&keywords="
ZOOPLA_MARKETINFO = "https://www.zoopla.co.uk/for-sale/houses/ipswich/?beds_min=3&price_max=500000&price_min=150000&property_sub_type=semi_detached&property_sub_type=detached&property_sub_type=terraced&property_sub_type=bungalow&q=ipswich&results_sort=newest_listings&search_source=for-sale&added=24_hours&feature=has_garden&feature=has_parking_garage&is_auction=false&is_retirement_home=false&is_shared_ownership=false"

DATAENTRY_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfwvTD1r9ZxZyNiUaW0YGqOk2D_DhjvlTxmyXyKTss3qP0iaA/viewform"

response = requests.get(RIGHT_MOV_MARKETINFO)
site = response.text
soup = BeautifulSoup(site, "html.parser")

listings = soup.find_all(class_="l-searchResult is-list")
addresses = []
link= []
price= []
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfwvTD1r9ZxZyNiUaW0YGqOk2D_DhjvlTxmyXyKTss3qP0iaA/viewform")
soup_lxml = BeautifulSoup(site, "lxml")
next_button = soup.find(class_="pagination-button pagination-direction pagination-direction--next")

for listing in listings:
    addresses.append(listing.find(class_="propertyCard-address").getText().strip())
    link.append(f'https://www.rightmove.co.uk{listing.find("a", class_="propertyCard-link").get("href")}')
    price.append(listing.find(class_="propertyCard-priceValue").getText().strip())
    address_input = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(listing.find(class_="propertyCard-address").getText().strip())
    time.sleep(1)
    price_input = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(listing.find(class_="propertyCard-priceValue").getText().strip())
    time.sleep(1)
    link_input = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(f'https://www.rightmove.co.uk{listing.find("a", class_="propertyCard-link").get("href")}')
    time.sleep(1)
    submit = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    time.sleep(1)
    go_again = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    go_again.click()
# zoopla_header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }
# response = requests.get(ZOOPLA_MARKETINFO, headers=zoopla_header)
# site = response.text
# soup = BeautifulSoup(site, "lxml")
# print(soup.prettify())
# listings = soup.find_all(class_="_1c58w6u2")
# print(listings)
# for listing in listings:
#     addresses.append(listing.find(class_="_1vvnr3j2 _1dgm2fc9").getText().strip())
#     print(listing.find(class_="_1vvnr3j2 _1dgm2fc9").getText().strip())


