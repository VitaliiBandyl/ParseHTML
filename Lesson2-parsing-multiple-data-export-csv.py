import requests
from bs4 import BeautifulSoup
import csv
import os


def get_html(url):
    r = requests.get(url)
    return r.text


def refind(s):
    r = s.split()[0][1:]
    return r.replace(',', '')


def init_csv_file():
    FILE = os.path.dirname(os.path.abspath(__file__)) + '\plugins.csv'
    if not os.path.exists(FILE):
        with open('plugins.csv', 'a') as f:
            writer = csv.writer(f, delimiter=';', lineterminator='\n')

            writer.writerow((
                'name',
                'url',
                'reviews'
            ))


def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\n')

        writer.writerow((
            data['name'],
            data['url'],
            data['reviews']
        ))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    section = soup.find_all('section')[1]
    plugins = section.find_all('article')

    for plugin in plugins:
        name = plugin.find('h3').text
        url = plugin.find('h3').find('a').get('href')
        r = plugin.find('span', class_='rating-count').text
        reviews = refind(r)

        data = {
            'name': name,
            'url': url,
            'reviews': reviews
        }

        init_csv_file()
        write_csv(data)


def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
