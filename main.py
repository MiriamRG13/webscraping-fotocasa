# Import libraries
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import csv
import pandas as pd
import time
import page_url

# Global variables
url = "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/todas-las-zonas/l?latitude=40.4096&longitude=-3.6862&combinedLocationIds=724,14,28,173,0,28079,0,0,0"
time.sleep(30)

# Configuration of webdriver to use Mozilla Firefox browser
driver = webdriver.Firefox()
driver.get(url)

# Class Definition
class HouseScraper():

    # Initial function
    def __init__(self):
        self.start_url = url
        self.base_url = "https://www.fotocasa.es"

    # Scrape function
    def scrape(self):

        # Writting csv headers
        if os.path.exists('buildings_information.csv'):
            os.remove('buildings_information.csv')

        with open("buildings_information.csv", "a") as csv_file:
            headers = ["Price", "Name", "Neighborhood", "Address", "Link"]
            writer = csv.DictWriter(csv_file, fieldnames = headers)
            writer.writeheader()

            page_url = self.start_url
            i = 0
            while page_url:

                # Call scrap_page function
                buildings = self.scrap_page(page_url)

                # Save information in csv file
                writer.writerow(buildings)

                # Getting next page's url
                driver.get(page_url)
                time.sleep(5)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                tmp = soup.find('div', attrs={ 'class': 're-Card re-Card--compact re-Card--landscape is-preloaded' })
                if i == 2:
                #if tmp == None:
                    break
                i = i + 1
                soup2 = BeautifulSoup(tmp)
                tmp2 = soup2.find('a')

                page_url = self.base_url + tmp2.attrs['href']

            print('end')

    def scrap_page(self, page_url, district):

        # Getting whole information (HTML) in page_url
        driver.get(page_url)
        soup = BeautifulSoup(driver.page_source, 'html_parser')
        
        # Searching information
        # Price
        price = soup.find('span', attrs = { 'class':'re-DetailHeader-price' })
        
        # Header
        header = soup.findAll('li', attrs = { 'class': 're-DetailHeader-featuresItem'})
        print(header)
        
