import requests

API_KEY = "98fbaf08955b40f78212d5a8df1277e3"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=%s" % API_KEY

def get_news_articles():
    # fetch the news articles
    response = requests.get(NEWS_API_URL)

    # return the articles in json format
    return response.json()['articles']
