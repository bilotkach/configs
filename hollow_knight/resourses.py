import requests
from bs4 import BeautifulSoup
import pandas as pd
import values as v
import mysql.connector as mc

def get_bosses_urls():
    r = requests.get(v.bosses_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    bosses_abc = soup.find('div', class_='category-page__members').find_all('div',
                                          class_='category-page__members-wrapper')
    bosses = []
    for letter in bosses_abc:
        bosses.extend([boss.find('a').get('href') for boss in letter.find('ul').find_all('li')])
    return bosses

def get_boss_data(boss_url):
    r = requests.get(boss_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    div = soup.find('div', class_='tooltip-content')
    if div.find('h2').text != 'Hornet':
        name = div.find('h2').text
    else:
        name = boss_url[boss_url.rfind('/') + 1:].replace('_', ' ')
    if div.find('div', attrs = {'data-source': 'health'}):
        health_txt = div.find('div', attrs = {'data-source': 'health'}).find('div').text
        if 'Nail' in health_txt:
            if 'Total' in health_txt:
                health = [int(h.strip()) for h in health_txt[health_txt.find('Total') + 6:health_txt.find('(')].split('/')]
            else:
                health = [int(h.strip()) for h in health_txt[:health_txt.find('(')].split('/')]
        elif 'Total' in health_txt:
            if 'Final Total' in health_txt:
                health = [int(health_txt[health_txt.find('Final Total') + 12:].strip())]*5
            else:
                if '-' in health_txt:
                    health_txt = health_txt[health_txt.find('Total') + 6:].strip()
                    health = [int(health_txt[health_txt.find('-') + 1:])]*5
                else:
                    health = [int(health_txt[health_txt.find('Total') + 6:].strip())]*5
        elif 'Minimum total to kill' in health_txt:
            health = [int(health_txt[health_txt.rfind('=') + 1:].strip())]*5
        elif '-' in health_txt:
            health = [int(health_txt[health_txt.find('-') + 1:health_txt.find('(')])]*5
        elif 'Trial' in health_txt or 'Elegant' in health_txt:
            health_txt = div.find('div', attrs = {'data-source': 'health'}).find('div').find('p').text
            health = [int(health_txt[:health_txt.find('(')].strip())]*5
        else:
            health = [int(health_txt)]*5
    else:
        health = ['NULL']*5
    data = pd.DataFrame({'lvl0' : [health[0]], 'lvl1' : [health[1]], 'lvl2' : [health[2]], 'lvl3': [health[3]], 'lvl4': [health[4]]}, columns = ['lvl0', 'lvl1', 'lvl2', 'lvl3', 'lvl4'], index = [name])
    # data = pd.Series(health, index=['Health(Nail_lvl0)','Health(Nail_lvl1)','Health(Nail_lvl2)','Health(Nail_lvl3)','Health(Nail_lvl4)'], name = name)
    return data
