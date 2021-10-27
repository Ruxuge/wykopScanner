import json


def readFiles():
    with open('data/posts.json', 'r') as file:
        file_data = json.load(file)
        for i in file_data['posts']:
            createUsersDataBase(i['author'], i['text'])


def createUsersDataBase(author, text):
    print(text)
    print(author)



def collect_user_data():
    readFiles()
