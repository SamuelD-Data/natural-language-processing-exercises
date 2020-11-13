from requests import get
from bs4 import BeautifulSoup
import os

def get_blog_articles():
    """
    No argument needed. Retrieves title and article text from 5 codeup webpages and returns as list of dictionaries.
    """
    # listing articles names
    articles = ['https://codeup.com/codeups-data-science-career-accelerator-is-here/',
    'https://codeup.com/data-science-myths/',
    'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/',
    'https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/',
    'https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/']
    
    # creating empty list
    l = []
    
    # using for loop to iterate through list of URLs
    for url in articles:
        # creating empty dictionary
        d = {}
        # specifying headers
        headers = {'User-Agent': 'Codeup Data Science'}
        # saving response from page
        response = get(url, headers=headers)
        # using beautiful soup to parse response
        soup = BeautifulSoup(response.text)
        # saving article body text
        article = soup.find('div', class_='jupiterx-post-content')
        # saving article title text
        title = soup.find('h1').text
        # storing article body and title in dictionary
        d['title'] = title
        d['article'] = article.text
        # appending dictionary to list
        l.append(d)
        
    # returning list when all article text added
    return l

    def new_funct(articles):
        """
        No argument needed. Retrieves body text and title from 5 different categories of inshorts articles
        """
    # saving articles urls in list
    articles = ['https://inshorts.com/en/read/business','https://inshorts.com/en/read/sports','https://inshorts.com/en/read/technology','https://inshorts.com/en/read/entertainment']
    # creating empty list
    l = []
    # iterating through each url
    for url in articles:
        # saving response from url page
        response = get(url)
        # parsing through response
        soup = BeautifulSoup(response.text)
        # finding all news cards within response
        cards = soup.find_all('div', class_='news-card')
        # iterating through cards
        for card in cards:
            # creating new dictionary
            d = {}
            # saving article title and body text
            title = (card.find('span', itemprop='headline').text)
            body = (card.find('div', itemprop='articleBody').text)
            # saving title and body text to dictionary
            d['title'] = title
            d['article'] = body
            # adding dictionary to list
            l.append(d)
    # returning list
    return l