import requests # for GET requests
import shutil # for writing images
from bs4 import BeautifulSoup # for searching webpages in an easy way
import os # for creating the needed directory

path = "../logos/LoL/OPL/"
''' path for the logos '''

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
        for div in upcoming_match_div.find_all(class_ = 'match-and-event-table__content-item paginator_0_data_class'):
            scrape_match_page(div.find('a')['href'])


def scrape_match_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))
    print(soup.find('main'))

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
#    with open('../team_urls/team_urls_opl.txt', 'r') as f: # team_urls_opl.txt contains our current PRM teams (they need to be the current teams from the current split as relevant information isn't present on normal team pages)
#        for line in f:
#            scrape_upcoming_matches(line)
    download_image('https://www.opleague.pro/styles/media/team/5404/Logo_30.webp?1698268749', 'test.webp')