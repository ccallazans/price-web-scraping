import requests
from bs4 import BeautifulSoup
import pandas

def access_page(url):
    try:
        request = requests.get(url)
        return request.content

    except BaseException as err:
        raise SystemExit(err)
    
def parse_page_content(page):
    soup = BeautifulSoup(page, 'html.parser')
    for div in soup.find_all(class_="DealGridItem-module__dealItem_2X_WLYkJ3-dM0LtXI9THcu DealGridItem-module__withBorders_2jNNLI6U1oDls7Ten3Dttl DealGridItem-module__withoutActionButton_2OI8DAanWNRCagYDL2iIqN"):
        print(div.prettify())




teste = access_page('https://www.amazon.com.br/deals?ref_=nav_cs_gb')
parse_page_content(teste)
