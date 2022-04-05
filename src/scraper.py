import requests
from bs4 import BeautifulSoup
import pandas

def access_page(url):
    try:
        request = requests.get(url)

    except BaseException as err:
        raise SystemExit(err)
    
    return request.content

def parse_page_content(page):
    soup = BeautifulSoup(page, 'html.parser')
    print(soup.prettify())



teste = access_page('https://www.amazon.com.br/deals?ref_=nav_cs_gb')
parse_page_content(teste)
