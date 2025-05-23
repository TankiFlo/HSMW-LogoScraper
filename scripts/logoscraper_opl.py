import requests # for GET requests
import shutil # for writing images
from bs4 import BeautifulSoup # for searching webpages in an easy way
import os # for creating the needed directory

path = "../logos/LoL/OPL/"
''' path for the logos '''

download_url = "https://www.opleague.pro/screenshot?url=https%3A%2F%2Fwww.opleague.pro%2Fstyles%2Fmedia%2Fteam%2F<TEAM-ID>%2FLogo_100.webp"
'''Replace <TEAM-ID> with the team id of the wanted team'''

def download_image(url, name):
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open(path + name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ', path + name)
    else:
        print('Image <- ' + name + ' -> Couldn\'t be retrieved')

def scrape_upcoming_matches(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    upcoming_match_div = soup.find(class_ = 'match-and-event-table__content-container')
    if upcoming_match_div is not None:
        for div in upcoming_match_div.find_all(class_ = 'img-text'):
            teamId = div.find('img')['src'].split('/')[6]
            url = download_url.replace('<TEAM-ID>', teamId)
            name = (div.find('img')['alt'] + ".png").replace('/', '').replace(':', '') # replace() for sanitization
            download_image(url, name)

def scrape_standings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    standing_table = soup.find(class_ = 'event-ranking__container opl-table --type-border --table-scroll')
    if standing_table is not None:
        for img in standing_table.find_all('img'):
            teamId = img['src'].split('/')[6]
            url = download_url.replace('<TEAM-ID>', teamId)
            name = (img['alt'] + ".png").replace('/', '').replace(':', '') # replace() for sanitization
            download_image(url, name)

if __name__ == '__main__':
    try: # create needed directory
        os.makedirs(path)
        print(f"Nested directories '{path}' created successfully.")
    except FileExistsError:
        print(f"One or more directories in '{path}' already exist.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # start scraping
    with open('../team_urls/team_urls_opl.txt', 'r') as f: # team_urls_opl.txt contains our current OPL teams
        for line in f:
            scrape_upcoming_matches(line.strip())
    with open('../team_urls/standing_urls_opl.txt', 'r') as f:
        for line in f:
            scrape_standings(line.strip())