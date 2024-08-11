import os
from bs4 import BeautifulSoup
import urllib.request as ur

def get_jury_list(base_url):
    if os.path.exists('temp/jury'):
        with open('temp/jury') as f:
            return f.read().strip().split('\n')
    
    return download_jury_list(base_url)

def download_jury_list(base_url):
    with ur.urlopen(base_url) as f:
        site = f.read()

    with open("temp/jury_list",  'wb') as f:
        f.write(site)

    soup = BeautifulSoup(site, features="html.parser")
    jury_heading = soup.find(text="Alle Jurymitglieder und ihre Lieblingslieder")
    jury_section = jury_heading.parent.parent
    jury_articles = jury_section.find_all('article')

    jury = []

    for article in jury_articles:
        link_elem = article.css.select('a.beitrag')[0]
        link = link_elem['href'][:-5].split("/")[-1]
        jury.append(link)

    with open("temp/jury",  'w') as f:
        f.write("\n".join(jury))

    return jury