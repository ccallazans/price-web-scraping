import json
import pandas as pd
from connection.utils import access_page_content
from extract.scrap import parse_page_content, open_json_file

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3'
})

JSON_PRODUCT_LINK = '/opt/airflow/src/products.json'
EXPORT_DATA_PATH = '/opt/airflow/src/temp/file.csv'

def main():

    items = open_json_file(JSON_PRODUCT_LINK)
    list_items = items["products"] 

    data = pd.DataFrame(columns=["product_id","name","price","link","image"])

    for link in list_items:
        page = access_page_content(link, HEADERS)

        try:
            collected_data = parse_page_content(page, link)
        except:
            raise Exception(f"\nERROR ON COLLECTING PRODUCT: {link}\n") 

        print("Collected Data: \n", json.dumps(collected_data, indent=4, default=str))
        data = data.append(collected_data, ignore_index=True)

    data.to_csv(EXPORT_DATA_PATH, index=False)

if __name__ == "__main__":
    main()