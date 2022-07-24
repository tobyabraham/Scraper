from requests_html import HTMLSession

s = HTMLSession()

iphone12 = 'https://slot.ng/apple-iphone-12-pro-128gb-single-sim-non-act.html'

def get_slot_product_url(product_link):
    url = product_link
    r = s.get(url)
    r.html.render(sleep=1, keep_page=True, scrolldown=1) #gets the page and render all js script
    price = r.html.find('h5.mb-0',first=True).text
    phone={
        'price':price
    }
    return phone['price']

print(get_slot_product_url(iphone12))    
