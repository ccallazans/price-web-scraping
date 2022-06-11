import requests
from extract.scrap import open_json_file

def access_page_content(url, header):
    request = requests.get(url, headers=header)
    
    return request.content


def simple_access_page(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Accept-Language': 'pt-BR'
    }
    request = requests.get(url, headers=header)
    return request


def verify_urls():
    items = open_json_file('/opt/airflow/src/products.json')
    list_items = items["products"] 

    for link in list_items:
        response = simple_access_page(link)
        if response.status_code != 200:
            raise Exception(f"\nStatus code error {response.status_code} on: {link}") 
    
    print("Products Link: OK!")

