import requests
from bs4 import BeautifulSoup

headers = {
    "user agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

product_link = []

r = requests.get(f'https://www.jumia.com.ng/apple-iphone-13-512gb-green-apple-authorized-134481519.html')
soup = BeautifulSoup(r.content, 'lxml')
name = soup.find('h1', class_='-fs20 -pts -pbxs').text
price = soup.find('span', class_='-b -ltr -tal -fs24').text
link = soup.find('meta', property = 'og:url')

phone = {
    'name': name,
    'price': price,
    'link': link["content"]
}

print(phone)

