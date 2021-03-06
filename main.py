# Import libraries
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# import requests
from bs4 import BeautifulSoup
import csv
#import pandas as pd
import time
# from page_url import scrap_page
import os

# Global variables
SCROLL_PAUSE_TIME = 0.5
url = "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/todas-las-zonas/l?latitude=40.4096&longitude=-3.6862&combinedLocationIds=724,14,28,173,0,28079,0,0,0"
# time.sleep(2)

# Configuration of webdriver to use Mozilla Firefox browser
driver = webdriver.Firefox(executable_path = 'C:/WebDriver/bin/geckodriver.exe')

# #Go to specific URL
driver.get(url)
time.sleep(10)

driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div[2]/button[2]').click()
time.sleep(3)
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(SCROLL_PAUSE_TIME)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break
pisos = driver.find_elements_by_class_name('re-Card-link')
print(pisos[1].get_attribute('href'))


# for e in pisos:
#     print(e.text)


# tmp=pisos[1].find_element_by_tag_name('a') #hay que extraer el href
# print(len(buildings))
# print(pisos[4].text)


# Without Selenium
# page = requests.get(url)
# soup = BeautifulSoup(page, 'html.parser')
# elementos = soup.findAll('article')
# print(len(elementos))

# base_url = "https://www.fotocasa.es"

# Writting csv headers
#if os.path.exists('buildings_information.csv'):
    #os.remove('buildings_information.csv')

#with open("buildings_information.csv", "a") as csv_file:
    #headers = ['Precio', 'Distrito','Tipo de inmueble', 'Habitaciones', 'Aseos', 'Superficie', 'Planta', 'Parking']
    #writer = csv.DictWriter(csv_file, fieldnames = headers)
    #writer.writeheader()

# Getting next page's url

#driver.get(page_url)
#time.sleep(5)
#soup = BeautifulSoup(url, 'html.parser')
#print(soup.prettify())
#page = requests.get(url).text
# soup = BeautifulSoup(url, 'html.parser')
# print(soup)
#buildings = soup.findAll('div', attrs={'class':"re-Card re-Card--compact re-Card--landscape is-preloaded"})
# print(len(buildings))
# print(buildings[5].prettify())
# for building in buildings:
    
#     path = building.find('a')

#     page_url = base_url + path.attrs['href']

#     # Call scrap_page function
#     # scrap_page(self, page_url, 'Chamartin')
  
#     print(page_url)

