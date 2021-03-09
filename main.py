# Import libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
from page_url import scrap_page
import os

# Global variables
SCROLL_PAUSE_TIME = 0.5
url = "https://www.fotocasa.es/es/comprar/viviendas/madrid-capital/todas-las-zonas/l?latitude=40.4096&longitude=-3.6862&combinedLocationIds=724,14,28,173,0,28079,0,0,0"

# Configuration of webdriver to use Mozilla Firefox browser
driver = webdriver.Firefox(executable_path = 'C:/WebDriver/bin/geckodriver.exe')

# Go to specific URL
driver.get(url)
time.sleep(10)

# Accept cookies
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div[2]/button[2]').click()
time.sleep(3)

# Get the screen height of the web
screen_height = driver.execute_script("return window.screen.height;")   
i = 1

# Scroll action
while True:
    # Scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(SCROLL_PAUSE_TIME)
    
    # Update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break
buildings = driver.find_elements_by_class_name('re-Card-link')

i = 0
for building in buildings:
    i += 1
    try:
        # Call scrap_page function
        districtLabel = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[4]/div[2]/div[1]/main/div[3]/section/article['+str(i)+']/div/div[2]/a/div[3]/h3')
        districtWaste = ''
        try:
            districtWaste = districtLabel.find_element_by_tag_name('span').text
        except:
            pass
            
        districtNoWaste = districtLabel.text[len(districtWaste):len(districtLabel.text)]
        districtSplitted = districtNoWaste.split(' ')
        district = districtSplitted[len(districtSplitted)-1]
        print(building.get_attribute('href'))
        scrap_page(building.get_attribute('href'), district)
    except:
        pass
