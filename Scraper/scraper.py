import requests
from bs4 import BeautifulSoup

base_url = 'https://www.jumia.com.ng/'

headers = {
    "user agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

product_link = []

for x in range(1,2):
    r = requests.get(f'https://www.jumia.com.ng/catalog/?q=samsung+phones&page={x}#catalog-listing')
    soup = BeautifulSoup(r.content, 'lxml')

    product_list = soup.find_all('article', class_='prd _fb col c-prd')
    for item in product_list:
        for link in item.find_all('a', href=True):
            product_link.append(base_url + link['href'])


# detail = 'https://www.jumia.com.ng/samsung-galaxy-a13-4gb128gb-memory-peach-126331734.html'


for link in product_link:
    r= requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    name = soup.find('h1', class_='-fs20 -pts -pbxs').text
    price = soup.find('span', class_='-b -ltr -tal -fs24').text

    samsung_devices = {
        'name': name,
        'price': price
    }

    print(samsung_devices)

