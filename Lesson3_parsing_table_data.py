import requests
import csv
from bs4 import BeautifulSoup


def get_html(url):
    html = requests.get(url)
    return html.text


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
        name = tds[1].find('a').text
        url = 'https://coinmarketcap.com' + tds[1].find('a').get('href')
        p = tds[3].find('a').text
        price = clean_price(p)

        data = {
            'name': name,
            'url': url,
            'price': price
        }
        write_csv(data)



def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
