import requests
from bs4 import BeautifulSoup
import csv
URL = 'https://misis.ru/university/struktura-universiteta/instituty/'


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('MISIS.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'], data['title_add'], data['addr']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    films = soup.find('div', class_='cols-flex').find_all('div', class_='col2_aspect')
    for film in films:
        try:
            title = film.find(class_='institute-item-head').find('h3').text.strip()

        except:
            title = ''

        try:
            title_add = film.find(class_='institute-item-head').find('p').text.strip()
        except:
            title_add = ''

        try:
            addr = film.find('div', class_='institute-item-head').find_all('p')[-1].text.strip()
        except:
            addr = ''
        data = {'title': title,
                'title_add': title_add,
                'addr': addr}
        write_csv(data)
get_page_data(get_html(URL))