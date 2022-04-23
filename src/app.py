import sys
import json
from product import access_page, parse_page_content, append_data
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
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

    for link in list_items:
        page = access_page(link, HEADERS)
        collected_data = parse_page_content(page, link)

        print("Collected Data: \n", json.dumps(collected_data, indent=4, default=str))
        append_data(collected_data)

    return False


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main("None", True)
    else:
        main(sys.argv[1])
