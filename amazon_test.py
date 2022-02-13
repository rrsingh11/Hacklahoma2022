# from bs4 import BeautifulSoup
# import urllib.request
# import requests
# import smtplib 

# price_list = []

# def check_price():
#     url = "https://www.amazon.com/HP-Generation-i5-1135G7-Graphics-15-dy2024nr/dp/B09FXFDGN3/?_encoding=UTF8&pd_rd_w=4AxNs&pf_rd_p=26dacb9e-c45b-4443-bb96-74ce304824a7&pf_rd_r=YFN11J94J2HCSMYVHM45&pd_rd_r=83ce2c08-b122-41b4-9473-551e6fb0b167&pd_rd_wg=pnIxR&ref_=pd_gw_exports_top_sellers_unrec&th=1"

#     req = requests.get(url)
#     soup = BeautifulSoup(req.text, "html.parser")

#     prices = soup.find(class_="a-offscreen").get_text()
#     prices = float(prices.replace(",", "").replace("$", ""))
#     price_list.append(prices)
#     # print(prices)

# PASSWORD = "08067589904"
# def send_email(message):
#     s = smtplib.SMTP("smtp.gmail.com", 587)
#     s.starttls()

#     s.login("successaje5@gmail.com", PASSWORD)
#     s.sendmail("successaje7@gmail.com", "successaje7@gmail.com", message)
#     s.quit()

from bs4 import BeautifulSoup
import urllib.request
import requests

url = "https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B099VMT8VZ/ref=lp_16225009011_1_2?th=1"

r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

#prices = soup.find(id="priceblock_ourprice").get_text()
price=soup.select_one(selector="#priceblock_ourprice")
#price = float(price.replace(",", "").replace("$", ""))
print(price)

