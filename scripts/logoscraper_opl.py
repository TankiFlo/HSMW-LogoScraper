import requests # for GET requests
import shutil # for writing images
from bs4 import BeautifulSoup # for searching webpages in an easy way
import os # for creating the needed directory

path = "../logos/LoL/OPL/"
''' path for the logos '''



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
    with open('../team_urls/team_urls_opl.txt', 'r') as f: # team_urls_opl.txt contains our current PRM teams (they need to be the current teams from the current split as relevant information isn't present on normal team pages)
        for line in f:
            # call scrape function here