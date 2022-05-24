import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint


f = open('news.csv', 'w', encoding='UTF-8_sig', newline='\n' )

f_object = csv.writer(f)
f_object.writerow(['Title', 'Date', 'Category', 'URL'])

for page_number in range(1,6):
    url = f'https://mtavari.tv/news/archive?page={page_number}'
    resp = requests.get(url)
    soup_all = BeautifulSoup(resp.text, 'html.parser')

    print(resp.status_code)
    print(resp.headers)


    #იმის გამო რომ div ტეგს არ ქონდა კლასი და ჰქონდა მხოლოდ სტილი გაწერილი ამიტომ სტილით პოვნის კოდი დავწერე
    soup = soup_all.find('div', style='box-sizing:border-box;min-height:1px;position:relative;padding-left:15px;padding-right:15px;width:[object Object];flex-basis:70.83333333333334%;flex-grow:0;flex-shrink:0;max-width:70.83333333333334%;margin-left:0%;right:auto;left:auto')
    all_news = soup.find_all('section')


    for each in all_news:
        news_title = each.find('div', class_='NewsItem__Text-sc-4tbadf-5 gZyskT').text
        # print(news_title)

        category = each.find('span', class_="NewsItem__Category-sc-4tbadf-10 gOsZnT").text
        # print(category)

        span_time = each.find('span', class_='NewsItem__Time-sc-4tbadf-9 kDTqdM')
        date = span_time.time.text
        # print(date)

        div_img = each.find('div', class_='NewsItem__Thumbnail-sc-4tbadf-4 GeHWl')
        img_url = div_img.img.attrs.get('src')
        # print(img_url)



        f_object.writerow([news_title, date, category, img_url])

    sleep(randint(15, 20))


