import requests
from bs4 import BeautifulSoup
import json


def add_comment_to_json(text, author):
    comment = {
        'text': text,
        'author': author
    }
    comment.update(comment)
    with open('data/comments.json', 'r+') as file:
        file_data = json.load(file)
        file_data["comments"].append(comment)
        file.seek(0)
        json.dump(file_data, file, indent=4)


def comments_scrapper():
    read_posts()


def read_posts():
    f = open('data/posts.json', "r")

    data = json.loads(f.read())
    j = 0

    for i in data['posts']:
        #j += 1
        url = i['link']
        comments_saver(url)
        #if j == 3:
            #break

    f.close()


def comments_saver(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    posts = soup.find_all('div', class_="wblock lcontrast dC")
    i = 0

    for post in posts:
        #i = i+1
        try:
            comment_author = post.find('a', class_='color-1 showProfileSummary').text
            comment_text = post.find('div', class_='text').text
        except AttributeError:
            continue
        add_comment_to_json(comment_text, comment_author)
        #if i == 3:
            #break


def save_data():
    print("end")


