import time
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    links = selector.css(".cs-overlay-link::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link = selector.css(".next.page-numbers::attr(href)").get()
    return link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".entry-title::text").get(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": 0,
        "summary": selector.xpath("string(//p)").get(),
        "tags": selector.css(".post-tags a::text").getall(),
        "category": selector.css(".meta-category span.label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    news = []
    count = 0

    while count < amount:
        html_content = fetch(url)
        links = scrape_novidades(html_content)
        for link in links:
            if count == amount:
                break
            noticia = scrape_noticia(fetch(link))
            news.append(noticia)
            count += 1
        url = scrape_next_page_link(html_content)

    create_news(news)
    return news
