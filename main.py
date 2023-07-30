
import requests
from bs4 import BeautifulSoup
MARKETINFO = "https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E689&minBedrooms=3&propertyTypes=detached%2Csemi-detached%2Cterraced&includeSSTC=false&mustHave=parking&dontShow=retirement%2CsharedOwnership&furnishTypes=&keywords="
DATAENTRY_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfwvTD1r9ZxZyNiUaW0YGqOk2D_DhjvlTxmyXyKTss3qP0iaA/viewform"

soup = BeautifulSoup()

website = requests.get(MARKETINFO)

