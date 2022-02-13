from bs4 import BeautifulSoup
import urllib.request
import requests

#url = "https://www.ebay.com/itm/203775765228?epid=14034142597&_trkparms=ispr%3D1&hash=item2f71fb6aec:g:UUQAAOSwyG5hzdZw&amdata=enc%3AAQAGAAACkPYe5NmHp%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsSDbb8Xz6YxVYplPlqqf7B3w2YDIl6ORCaQvDw5FUWP3slvpyKlrhUZs1Mf0%252Fx%252BmtgaA0CGhh%252BuiZ8vU2YbfBtv2lVJUq7UFPomxCB%252BydfnjVlh0GDWBK2tghQDXglrp%252BwR%252BoXB93U%252BjV4e9nrpUvwRJCkvmz4iUwnkIcVTzAkyNffekLIEwO3zKqKBUh2GiLrwQS2HdHiaQfpIc6PaLZgnAStqPTi%252F6tvoyXpgpyde7vn%252Fvm%252BqE4IEHtUiNLd8pI%252FQg7I28Rzxtx21mYXCwA1oYuTxfFnknFG0tVZ9hihm%252FwV4wq3EQk0ReSB9Gb7oXfnXVtTCs1Mpw06Vk1B%252Ft6DyAXN4BgUxZnDZpZJIEGO2MNS9gOVbgxrARO9ikSZYsk9VdVELe6oj9ARQwq3ldFE41U%252FgNS2%252B9Nqw0vz01PPojCLRRUeJNjUBDcUib8WcalNuU3PB1AXS0149SnVGAbBnUyq23xoegCX3UprdIn8conFegKdU8pSs1TYZ5gLgNI8hmQP6ySBSFZcvkuJR2TKoRrRCRvSxmgMHRXMHrxzQB%252BoVDJSu4vI1Nh02rMVUtAGT4PfZSbmFZVm%252BE0dtv61vW57025Ds9a67SYVT1MRrzztHCZFNOu8idvyMWyvI0AUbUwkeZ44IlSL3g1WBX%252BT%252B4Lrdkq5Pc1ANlniSLq4rfn4tsz6avN7Dw54iRrAcgrzWkXM4Wwt%252F%252FcBGnvOfvU4%252BoR7OWvrylxmweR%252Fwl3BZDf4lqIGEXR6R2a3PcLwi5raU15bzlNSc%252BzY8tC0Qrbd2kgETUQZHAKyvZS5Pmejjy3JhA0oG13prEtbVyaY%252Fm2L%7Cclp%3A2499334%7Ctkp%3ABFBM0NWOud5f&var=504217486140"
url = input("Enter the url: ")

req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

price = soup.find('span', attrs={'itemprop':'price'}).get_text()

#prices = float(prices.replace(",", "").replace("$", ""))
print(price)
print("The current price of the product is : {0}".format(price))