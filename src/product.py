import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

DATA_FOLDER = 'data/'


def access_page(url, header):
    request = requests.get(url, headers=header)
    
    return request.content


def get_product_name(page):
    find_name = page.find_all('span', id="productTitle")
    find_name = find_name[0].contents
    
    if len(find_name) == 0:
        return "Empty Name"

    return find_name[0].strip(' ')


def get_product_price(page):
    find_price = page.find_all('span', class_="a-price-whole")
    find_price = find_price[0].contents
    
    if len(find_price) == 0:
        return "Empty Price"
    
    return find_price[0].strip(' ')


def get_product_link(page):
    find_link = page.find_all('link', rel="canonical")
    
    if len(find_link) == 0:
        return "Empty Link"
    
    return str(find_link[0]).split(' ')[1].split('href=')[1].strip('"')


def get_product_image(page):
    find_image = page.find_all('img', id="landingImage")
    
    img_pos = str(find_image[0]).find("src=")
    list_links = str(find_image[0])[img_pos:].split(' ')
    image = list_links[0].split('src=')[1]
    
    return image.strip('"')


def to_dict(*args):

    dictionary = {
        "Name": args[0],
        "Price": args[1],
        "Link": args[2],
        "Image": args[3]
    }

    return dictionary


def parse_page_content(page):
    soup = BeautifulSoup(page, 'html.parser')
    
    product_name = get_product_name(soup)
    product_price = get_product_price(soup)
    product_link = get_product_link(soup)
    product_image = get_product_image(soup)
    
    return to_dict(product_name, product_price, product_link, product_image)


def append_data(json_data):
    if os.path.exists('src/' + DATA_FOLDER + 'prices.csv'):
        data = pd.read_csv('src/' + DATA_FOLDER + 'prices.csv')
    else:
        data = pd.DataFrame(columns=["Name","Price","Link","Image"])
        
    data = data.append(json_data, ignore_index=True)
    return data.to_csv('src/' + DATA_FOLDER + 'prices.csv', index=False)
