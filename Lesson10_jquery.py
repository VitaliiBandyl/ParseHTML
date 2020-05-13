import csv

import requests
from bs4 import BeautifulSoup


def get_html(url):
    header = {'user-agent': "Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/81.0.4044.138 Safari/537.36"}
    r = requests.get(url, headers=header)
    return r.text


def write_csv(data):
    with open('catertrax.csv', 'a') as f:
        order = ['author', 'account', 'traxer_since', 'email', 'telephone', ]
        writer = csv.DictWriter(f, fieldnames=order, delimiter=';', lineterminator='\n')
        writer.writerow(data)


def get_card(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', id='testimonial-2364-3-0-0').find_all('div', class_='author-details')
    print(len(ts))
    print(ts)
    return ts


def get_page_data(ts):
    for article in ts:
        try:
            author = article.find('p', class_='testimonial-author').contents[
                0].strip()
        except:
            author = ''
        try:
            account = article.find('p', class_='testimonial-author').find('span',
                                                                          class_='account-name').text.strip()
        except:
            account = ''
        try:
            traxer_since = article.find('p', class_='traxer-since').contents[
                1].strip()
        except:
            traxer_since = ''
        try:
            email = article.find('ul', class_='testimonial-meta').find('li',
                                                                       class_='email').text.strip()
        except:
            email = ''
        try:
            telephone = article.find('ul', class_='testimonial-meta').find('li',
                                                                           class_='tel').text.strip()
        except:
            telephone = ''

        data = {
            'author': author,
            'account': account,
            'traxer_since': traxer_since,
            'email': email,
            'telephone': telephone
        }

        write_csv(data)


def main():
    page = 1
    while True:
        url = f'https://catertrax.com/why-catertrax/traxers/page/{str(page)}/?themify_builder_infinite_scroll=yes'
        content = get_card((get_html(url)))
        if content:
            get_page_data(content)
            page += 1
        else:
            break


if __name__ == '__main__':
    main()
