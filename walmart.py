# from bs4 import BeautifulSoup
# import urllib.request
# import requests
# import smtplib 

# #price_list = []

# #def check_price():"h
# url = "https://www.walmart.com/ip/SteelSeries-Apex-Pro-Mechanical-Gaming-Keyboard-Black/526303144"
# re = requests.get(url)
# soup = BeautifulSoup(re.text, "html.parser")

# #prices = soup.find(class_="a-offscreen").get_text()
# prices = soup.find(itemprop="price")
# print(prices)
#     #prices = float(prices.replace(",", "").replace("$", ""))
#     #price_list.append(prices)

from bs4 import BeautifulSoup
import urllib.request
import requests

url = "https://www.walmart.com/ip/SteelSeries-Apex-Pro-Mechanical-Gaming-Keyboard-Black/526303144"

wal = requests.get(url)
soup = BeautifulSoup(wal.text, "html.parser")

prices = soup.find('span',{'itemprop':"price"}).get_text()
prices = float(prices.replace(",", "").replace("$", ""))
print(prices)