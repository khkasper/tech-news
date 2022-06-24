from tech_news.database import search_news
from datetime import datetime

MONTHS = {
    "01": "janeiro",
    "02": "fevereiro",
    "03": "março",
    "04": "abril",
    "05": "maio",
    "06": "junho",
    "07": "julho",
    "08": "agosto",
    "09": "setembro",
    "10": "outubro",
    "11": "novembro",
    "12": "dezembro",
}


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "-i"}})
    title_results = []
    for news in news_list:
        title_results.append((news["title"], news["url"]))
    return title_results


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        year, month, day = date.split("-")
        data = f"{int(day)} de {MONTHS[month]} de {year}"
        news_list = search_news({"timestamp": data})
        date_results = []
        for news in news_list:
            date_results.append((news["title"], news["url"]))
        return date_results


# Requisito 8
def search_by_tag(tag):
    news_list = search_news({"tags": {"$regex": tag, "$options": "-i"}})
    tag_results = []
    for news in news_list:
        tag_results.append((news["title"], news["url"]))
    return tag_results


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
