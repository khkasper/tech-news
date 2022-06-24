from tech_news.database import db, find_news
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
    news_list = find_news()
    categories_list = list(news["category"] for news in news_list)
    categories_count = {}
    for category in categories_list:
        if category in categories_count:
            categories_count[category] += 1
        else:
            categories_count[category] = 1
    sorted_categories = sorted(
        categories_count.items(), key=lambda x: x[1], reverse=True
    )
    top_5 = []
    for key, _ in sorted_categories:
        top_5.append(key)
    return top_5


# https://stackoverflow.com/questions/8109122/how-to-sort-mongodb-with-pymongo
