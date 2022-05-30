import sys
import json
import pandas as pd
from etl import access_page, parse_page_content, append_data
from connection import upload_file
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3'
})

def open_json_file(path):
    f = open(path)
    return json.load(f)

def main(arg, product_file=False):
    if product_file == True:
        items = open_json_file('src/products.json')
        list_items = items["products"] 
    else:
        list_items = [arg]

    data = pd.DataFrame(columns=["product_id","name","price","link","image"])

    for link in list_items:
        page = access_page(link, HEADERS)
        collected_data = parse_page_content(page, link)

        print("Collected Data: \n", json.dumps(collected_data, indent=4, default=str))
        data = data.append(collected_data, ignore_index=True)

    append_data(data)
    upload_file(data)

    return False


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main("None", True)
    else:
        main(sys.argv[1])
