import sys
import json
from product import access_page, parse_page_content, append_data
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
})


def main(link):
    page = access_page(link, HEADERS)
    collected_data = parse_page_content(page)

    print("Collected Data: \n", json.dumps(collected_data, indent=4))
    return append_data(collected_data)


if __name__ == "__main__":
    main(sys.argv[1])
