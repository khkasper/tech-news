from tech_news.database import db
from pymongo import ASCENDING, DESCENDING


# Requisito 10
def top_5_news():
    top_5 = []
    news_list = (
        db.news.find()
        .sort([("comments_count", DESCENDING), ("title", ASCENDING)])
        .limit(5)
    )
    for news in news_list:
        top_5.append((news["title"], news["url"]))
    return top_5


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""


# https://stackoverflow.com/questions/8109122/how-to-sort-mongodb-with-pymongo
