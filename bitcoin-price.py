import datetime
import dominate
from dominate.tags import *
from dominate.util import raw
import json
import os.path
import pytz
import requests

def bitcoin_price_decimal():
    url = "https://api.coindesk.com/v1/bpi/currentprice/USD.json"
    r = requests.get(url)
    return round(float(r.json()["bpi"]["USD"]["rate"].replace(',', '')), 2)

def bitcoin_price_thousand():
    return bitcoin_price_decimal() // 1000

def bitcoin_price_display(mode):
    price_string = '$'

    if mode == 'decimal':
        price_string += str(bitcoin_price_decimal())
    elif mode == 'thousand':
        price_string += str(bitcoin_price_thousand()).replace('.0', '') + 'K'

    price_string += ' USD'
    
    return price_string

def build_btc_price_doc():
    doc = dominate.document(title='Bitcoin (BTC) Price')

    with doc.head:
        link(rel='stylesheet', href='style.css')
        link(rel='preconnect', href='https://fonts.gstatic.com')
        link(href='https://fonts.googleapis.com/css2?family=Space+Mono&display=swap')

    with doc:
        with div():
            attr(cls='body')

            with div():
                attr(cls='flex-container')
            
                with div():
                    attr(cls='price')
                    span(bitcoin_price_display('decimal'))

                with div():
                    attr(cls='price-mobile')
                    span(bitcoin_price_display('thousand'))

                with div():
                    attr(cls='timestamp')
                    span(current_timestamp())

    return str(doc)

def current_timestamp():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    
    return utc_now.isoformat()

def display_current_bitcoin_price():
    print("Current Bitcoin price:")
    print(bitcoin_price_display('decimal'))
    print(current_timestamp())

def save_html_doc(document, target_file):
    with open(target_file, 'w') as out_file:
        out_file.write(str(document))

def main():
    display_current_bitcoin_price()
    save_html_doc(
        document=build_btc_price_doc(),
        target_file='docs/index.html'
    )

main()
