#!/usr/bin/env python3.10

import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

links = []

def verify_href(href):
    if (href.find("/wiki/") == -1):
        return False
    elif (('(' in href and ')' in href)):
        return True
    return True

def take_first_href(soup):
    content = soup.find(id="mw-content-text")
    links_lst = content.select('p>a')

    if (len(links_lst) == 0):
        print(f'It leads to a dead end!')
        return None
    for l in links_lst:
        if (verify_href(l['href']) and not l.find_parent('i')):
            return l

def safe_history(link_title):
    #before save to history verify if it most end
    if (link_title == 'Philosophy'):
        print(link_title)
        print(f'{len(links)} roads from {sys.argv[1]} to philosophy!')
        return False
    if (links):
        if (link_title in links):
            print(link_title)
            print(f'It leads to an infinite loop!')
            return False

    links.append(link_title)
    print(link_title)


def init_road(research):
    url = f'https://en.wikipedia.org{research}'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, 'html.parser')

    if (response.status_code != 200):
        print(f'Error: {response.reason}. Unable to continue.')
        return
    scrapped_link = take_first_href(soup=soup)
    if (scrapped_link is None):
        return
    linkToScrape = scrapped_link['href']
    link_title = scrapped_link['title']

    if (safe_history(link_title=link_title) == False):
        return

    init_road(linkToScrape)

if __name__ == "__main__":
    if (len(sys.argv) > 2 or len(sys.argv) == 1):
        print('Use: ./roads_to_philosophy.py "<research>"')
        sys.exit(1)
    uri_sintax = quote(sys.argv[1])
    research = '/wiki/' + uri_sintax
    init_road(research=research)
