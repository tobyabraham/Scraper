#import requests

import time

import pandas as pd
from requests_html import HTMLSession

# products = r.html.xpath('//*[@id="maincontent"]/div/div[1]/div[4]', first=True) justfones
# URL = 'https://www.jumia.com.ng/phones-tablets'

s = HTMLSession()
phonelist = []

def request(url):
    r = s.get(url)
    r.html.render(sleep=1)
    return r.html.xpath('//*[@id="jm"]/main/div[2]/div[3]/section/div[1]', first=True)

def parse(products):
    for item in products.absolute_links:
        r = s.get(item)
        try:
            name = r.html.find('div.-df.-j-bet > div > h1', first=True).text
            price = r.html.find('div.-hr.-mtxs.-pvs > div > span', first=True).text
            link = r.html.find('head > meta:nth-child(7)', first=True).text
        except:
            name= 'none'
            price= 'none'
            link= 'none'

        phone = {
            'name' : name,
            'price' : price,
            'link' : link
        }
        phonelist.append(phone)

def output():
    df = pd.DataFrame(phonelist)
    df.to_csv('phonelist.csv')
    print('Saved to csv file.')


#https://www.jumia.com.ng/phones-tablets/?q=samsung%2F&page=3#catalog-listing
x=1
item = input("Enter search item:")
while True:
    try:
        products = request(f'https://www.jumia.com.ng/catalog/?q={item}&page={x}#catalog-listing')
        print('Getting items from page.')
        parse(products)
        print('Total Items: ', len(phonelist))
        x=x+1
        time.sleep(2)
    except:
        print('No more items!')
        break
output()    
