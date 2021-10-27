import requests
from bs4 import BeautifulSoup
import json


def add_post_to_json(title, text, author, link):
    post = {
        'title': title,
        'text': text,
        'author': author,
        'link': link
    }
    post.update(post)
    with open('data/posts.json', 'r+') as file:
        file_data = json.load(file)
        file_data["posts"].append(post)
        file.seek(0)
        json.dump(file_data, file, indent=4)


def post_scrapper():
    url = 'https://www.wykop.pl'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    posts = soup.find_all(class_="lcontrast m-reset-margin")

    for post in posts:
        post_author = post.find('div', class_='fix-tagline')
        try:
            post_author = post.find('a', class_='color-2 affect').text
        except AttributeError:
            continue
        try:
            post_text = post.find('p', class_='text')
        except AttributeError:
            continue
        try:
            post_title = post.find('a').text
        except AttributeError:
            continue
        try:
            link = post.find('a')
            post_link = link.get('href')
        except AttributeError:
            continue
        add_post_to_json(post_title, post_text, post_author, post_link)
