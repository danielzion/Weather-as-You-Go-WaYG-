# news web scrapper
from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

# scrap weather news articles from the web (from a popular website like nasa)
# get the relevant html tags as text
# integrate the scrapped html tags into our system


# website url to be scrapped
url = "https://news.un.org/en/news/topic/climate-change"

# getting the url request
url_request = requests.get(url)

# storing the request
website_coverpage = url_request.content

# the soup element to enable web scrapping
website_soup = BeautifulSoup(website_coverpage, 'html.parser')

# locating the elements needed
coverpage_news = website_soup.find_all('div', class_='view-content')

# number of articles to be displayed
number_of_articles = len(coverpage_news)

# the content, links and titles
news_content = []
list_links = []
list_titles = []

for n in np.arange(0, number_of_articles):
    # getting the link of the articles
    link = coverpage_news[n].find('a')['href']
    list_links.append(link)
    full_link = "https://news.un.org" + link

    # getting the titles
    tilte = coverpage_news[n].find('a').get_text()
    list_titles.append(tilte)

    # reading the contents
    article = requests.get(full_link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, "html5lib")
    body = soup_article.find_all('div', class_='srcss-11r1m41-RichTextComponentWrapper ep2nwvo0')
    """x = body.find('p', class_='ssrcss-7uxr49-RichTextContainer')

    # unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(x)):
        list_paragraphs.append(paragraph = x[p].get_text())
        final_article = " ".join(list_paragraphs)

    news_content.append(final_article)"""

# storing in a dataframe
df_features = pd.DataFrame (
    {
        'Article Content': news_content
    }
)

df_show_info = pd.DataFrame (
    {
        'Ariticle Title': list_titles,
        'Article Link': list_links
    }
)

print(df_show_info)