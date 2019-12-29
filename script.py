import bs4
import pandas as pd
import requests
from pprint import pprint


url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
def get_page_contents(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"})
    # print (page)
    return bs4.BeautifulSoup(page.text, "html.parser")

soup = get_page_contents(url)
movies = soup.findAll('h3', class_='lister-item-header')
# titles = [movie.find('a').text for movie in movies]

titles = []
for movie in movies:
    # movie.find('a').text 
    titles.append(movie.find('a').text)

pprint(titles)
