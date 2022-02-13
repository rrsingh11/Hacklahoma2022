from bs4 import BeautifulSoup
import urllib.request
import requests

#url = "https://www.jolinaforuno.top/ProductDetail.aspx?iid=336462430&pr=57.88"
try:
    url = input('Enter the url: ')

except Exception:
    pass

req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

prices = soup.find(class_="current_price").get_text()
prices = float(prices.replace(",", "").replace("$", ""))

print("This is the price of the product {0} Dollars".format(prices))
