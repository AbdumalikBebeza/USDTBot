from pydoc import html

from bs4 import BeautifulSoup as BS
import requests
from pprint import pprint

URL = "https://www.binance.com/en-GB/price/tether"

HEADERS = {
    'Auser_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/'
              '*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}


def get_url(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    if req.status_code == 200:
        return req
    else:
        return None


def get_data(html):
    soup = BS(html, "html.parser")
    item = soup.find("div", class_="css-3j2kqe")
    # print(item)

    usdt_price = item.find("div", class_="css-dbxihu").getText().split(" ")

    return usdt_price


def parser():
    try:
        html = get_url(URL)
        data = get_data(html.text)
        return data
    except AttributeError:
        return None



