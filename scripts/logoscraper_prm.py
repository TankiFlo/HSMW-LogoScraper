import image_downloader
import requests # for GET requests
from bs4 import BeautifulSoup # for searching webpages in an easy way
import os # for creating the needed directory

path = "../logos/PRM/"
''' path for the logos '''

def scrape_team_page(url):
    ''' Scrapes the given URL (the Primeleague Website for a team) for its upcoming/completed matches and calls scrape_match_page to scrape those '''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    counter = 0 # set up a counter to only ever take the first href (because PRM has 3 times the same href: for team name A, the score and team name B)
    for a in soup.find(class_='section-block league-stage-matches').find_all('a'):
        counter += 1
        if '/matches/' in a['href'] and counter%3 == 0: # only takes every third URL for less traffic and a faster program, see above for why
            scrape_match_page(a['href'])

def scrape_match_page(url):
    ''' Scrapes the given URL (the Primeleague Website for a match between 2 teams) for the images and alt texts of those to then download them in "/logos/..." '''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for img in soup.find_all('img'):
        if 'team_logos' in img['src']:
            name = img['alt'] + ".jpg"
            ''' file name for the logos '''
            image_downloader.download_image(img['src'], path, name)

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
    with open('../team_urls/team_urls_prm.txt', 'r') as f: # team_urls_prm.txt contains our current PRM teams (they need to be the current teams from the current split as relevant information isn't present on normal team pages)
        for line in f:
            scrape_team_page(line.strip())