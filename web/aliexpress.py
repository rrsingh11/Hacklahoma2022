from bs4 import BeautifulSoup
import urllib.request
import requests
from requests_html import AsyncHTMLSession

import pyppdf.patch_pyppeteer

#url = "https://www.aliexpress.com/item/1005003799989432.html?spm=a2g0o.productlist.0.0.501a27c9qJuPw5&algo_pvid=2c25b791-e436-4da3-b07c-10a1a31e99c2&aem_p4p_detail=202202130735359525307152133500155926366&algo_exp_id=2c25b791-e436-4da3-b07c-10a1a31e99c2-0&pdp_ext_f=%7B%22sku_id%22%3A%2212000027207786713%22%7D&pdp_pi=-1%3B4165.93%3B-1%3B-1%40salePrice%3BNGN%3Bsearch-mainSearch"
try:
    url = input("Enter the url: ")
except Exception:
    print("Invalid input")
    pass

asession = AsyncHTMLSession()
html = requests.get(url)

cookies=html.cookies

soup = BeautifulSoup(html.text, "html.parser")


    r = await asession.get(url)
    await r.html.arender()



#price = soup.find('span', attrs={'class_':'product-price-value'}).get_text()
price = r.html.find('.product-price-value')
absPrice = price[0].text.replace('US', '').strip()
#prices = float(prices.replace(",", "").replace("$", ""))
print(absPrice)
print("The current price of the product is : {0}".format(absPrice))