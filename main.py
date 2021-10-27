from urllib3.util import url

from functions import dataCollector
from scrapper import postScrapper, commentsScrapper


if __name__ == '__main__':
    postScrapper.post_scrapper()
    commentsScrapper.comments_scrapper()
    dataCollector.collect_user_data()


