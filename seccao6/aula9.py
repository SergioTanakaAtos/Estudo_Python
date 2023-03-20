import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'
response = requests.get(url)
raw_html = response.text 
parset_html =BeautifulSoup(raw_html ,'html.parser')


top_jobs_title = parset_html.select_one('#intro > div > div > article > h2')
if top_jobs_title is not None:  
    article = top_jobs_title.parent 
    print(article)
    if article is not None:
        for p in article.select('p'):
            print(p)