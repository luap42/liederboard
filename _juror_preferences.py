import os
from bs4 import BeautifulSoup
import urllib.request as ur

def get_juror_preferences(base_url, juror):
    if os.path.exists(f'temp/juror_{juror}'):
        with open(f'temp/juror_{juror}') as f:
            return [i.split('|') for i in f.read().strip().split('\n')]
    
    return download_juror_preferences(base_url, juror)

def download_juror_preferences(base_url, juror):
    with ur.urlopen(f"{base_url}/{juror}.html") as f:
        site = f.read()

    with open(f"temp/juraws/{juror}",  'wb') as f:
        f.write(site)

    soup = BeautifulSoup(site, features="html.parser")
    pref_heading = soup.find(text="Meine Top 10")
    pref_section = pref_heading.parent.parent
    pref_table = pref_section.find('table')

    preferences = []

    for pref in pref_table.find_all('tr'):
        pref_song = pref.css.select('.count3')[0].text
        pref_band = pref.css.select('.count2')[0].text  

        preferences.append((pref_song, pref_band))

    with open(f"temp/juror_{juror}",  'w') as f:
        f.write("\n".join([i[0] + '|' + i[1] for i in preferences]))
    
    return preferences