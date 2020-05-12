import csv

import requests


def get_response(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('liveinternet.csv', 'a') as f:
        order = ['name', 'url', 'description', 'traffic', 'percent']
        writer = csv.DictWriter(f, fieldnames=order, delimiter=';', lineterminator='\n')
        writer.writerow(data)


def main():
    for page in range(1, 6895):
        url = f'https://www.liveinternet.ru/rating/ru//today.tsv?page={page}'
        """URL should be taken from Chrome DevTools --> Network --> XHR"""
        response = get_response(url).strip().split('\n')[1:]
        for row in response:
            columns = row.strip().split('\t')
            name = columns[0]
            url = columns[1]
            description = columns[2]
            traffic = columns[3]
            percent = columns[4]

            data = {
                'name': name,
                'url': url,
                'description': description,
                'traffic': traffic,
                'percent': percent
            }

            write_csv(data)


if __name__ == '__main__':
    main()
