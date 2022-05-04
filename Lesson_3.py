import json
import requests
from bs4 import BeautifulSoup as bs

quotes_list = []
with open('quotes_data_tmp.json', 'w') as jf:
    for page_number in range(1, 11):
        print(f'Start scraping page #{page_number}')
        url = f'https://quotes.toscrape.com/page/{page_number}/'
        req = requests.get(url)
        if req.status_code == 200:
            html = bs(req.content, 'html.parser')
            all_quotes = html.select('div[class=quote]')
            print(len(all_quotes))
            for quote_number, quote in enumerate(all_quotes, 1):
                print(f'\tStart scraping quote #{quote_number} from {len(all_quotes)}')
                quote_text = quote.select_one('span[class=text]').text[1:-1]
                quote_author = quote.select_one('span small').text
                quotes_tags = [tag.text for tag in quote.select('div[class=tags] a[class=tag]')]
                quote_dict = {
                    'quote_text': quote_text,
                    'quote_author': quote_author,
                    'quotes_tags': quotes_tags,
                    'source': 'quotes.toscrape.com'
                }
                quotes_list.append(quote_dict)

                json.dump(quote_dict, jf)
                print(f'\t\tSaved quote #{quote_number} from {len(all_quotes)}')

        else:
            print(f'Ошибка: {req.status_code}')

    with open('quotes_data.json', 'w') as jf:
        json.dump(quotes_list, jf)
