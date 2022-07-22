from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests

url = 'https://www.jumia.com.ng/phones-tablets'

s = HTMLSession()
r = s.get(url)

r.html.render(sleep=1)

products = r.html.xpath('//*[@id="jm"]/main/div[2]/div[3]/section/div[1]', first=True)

for item in products.absolute_links:
    r = s.get(item)
    print(r.html.find('div.-fs0 -pls -prl', first=True).text)