import csv
from multiprocessing import Pool

import requests


def get_response(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('liveinternet.csv', 'a') as f:
        order = ['name', 'url', 'description', 'traffic', 'percent']
        writer = csv.DictWriter(f, fieldnames=order, delimiter=';', lineterminator='\n')
        writer.writerow(data)


def get_page_data(text):
    data = text.strip().split('\n')[1:]

    for row in data:
        columns = row.strip().split('\t')
        name = columns[0]
        url = columns[1]
        description = columns[2]
        traffic = columns[3]
        percent = columns[4]

        data = {'name': name,
                'url': url,
                'description': description,
                'traffic': traffic,
                'percent': percent
                }

        write_csv(data)


def make_all(url):
    text = get_response(url)
    get_page_data(text)


def main():
    url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'
    urls = [url.format(str(i)) for i in range(1, 6895)]

    with Pool(20) as p:
        p.map(make_all, urls)


if __name__ == '__main__':
    main()
