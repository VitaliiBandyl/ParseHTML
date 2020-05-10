import requests
import csv
import re
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def write_csv(data):
    with open('cms.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\n')

        writer.writerow((
            data['name'],
            data['url'],
            data['price']
        ))


def clean_price(s):
    price = s[1:].replace(',', '')
    return price


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        try:
            name = tds[1].find('a').text.strip()
        except Exception:
            name = ''

        try:
            url = 'https://coinmarketcap.com' + tds[1].find('a').get('href')
        except Exception:
            url = ''
        try:
            p = tds[3].find('a').text.strip()
            price = clean_price(p)
        except Exception:
            price = ''

        data = {
            'name': name,
            'url': url,
            'price': price
        }
        write_csv(data)


def main():
    url = 'https://coinmarketcap.com/'

    while True:
        html = get_html(url)
        get_page_data(html)
        soap = BeautifulSoup(html, 'lxml')
        pattern = 'Next'

        try:
            url = 'https://coinmarketcap.com' + \
                  soap.find('a', class_='cmc-link', text=re.compile(pattern)).get('href')
        except Exception:
            break


if __name__ == '__main__':
    main()
