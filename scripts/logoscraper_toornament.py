import image_downloader
import os # for creating the needed directory
from selenium import webdriver # for getting dynamic webpages
from bs4 import BeautifulSoup # for searching webpages in an easy way
import time

path = "../logos/Toornament/"
''' path for the logos '''

def scrape_participants(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    url = "https://play.toornament.com/de/tournaments/8635309642524221440/participants/"
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    team_divs = soup.find_all(class_ = "concerto block custom block")

    for div in team_divs:
        img = div.find('img')
        if img is not None:
            text_div = div.find(class_ = "text sized concerto block align-start")
            image_downloader.download_image(img['src'].replace("medium", "large"), path, text_div.getText()+".png")

    driver.quit()

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
    with open('../team_urls/team_urls_toornament.txt', 'r') as f: # team_urls_opl.txt contains our current OPL teams
        for line in f:
            scrape_participants(line.strip())