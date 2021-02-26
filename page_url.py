# Import libraries
import requests
from bs4 import BeautifulSoup
import csv
import time
import pandas as pd
from home import Home

# def scrap_page(self, page_url, district):
# Global variables
url = 'https://www.fotocasa.es/es/comprar/vivienda/madrid-capital/aire-acondicionado-calefaccion-trastero-ascensor-internet-no-amueblado/157915887/d'
time.sleep(5)

# Getting whole information (HTML) in page_url
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

with open('info.csv', 'a') as csv_file:
    headers = ['Price', 'District', 'Rooms', 'Baths', 'Size', 'Floor']
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    
    district = 'Chamartin'
    home = Home(url, district)
    
    # Searching information
    # Price
    price = soup.find('span', attrs = { 'class':'re-DetailHeader-price' }).string
    b = slice(len(price)-2)
    home.price = price[b]

    # Header
    header = soup.findAll('li', attrs = { 'class': 're-DetailHeader-featuresItem'})
    for i in header:
        element = i.findAll('span')
        tmp = element[len(element)-2].get_text().split(' ')
        number = tmp[0]
        if len(tmp) != 1:
            type = tmp[1]
            if type == 'habs.':
                home.rooms = number
            if type == 'baños':
                home.baths = number
            if type.startswith('m'):
                home.size = number
            if type == 'Planta':
                a = slice(len(number)-1)
                home.floor = number[a]
        else:
            number = element[len(element)-1].get_text()

    writer.writerow({'Price':    home.price, 
                     'District': home.district, 
                     'Rooms':    home.rooms,
                     'Baths':    home.baths, 
                     'Size':     home.size, 
                     'Floor':    home.floor})

    print('Precio:', home.price)
    print('Distrito', home.district)
    print('Nº Habitaciones:', home.rooms)
    print('Nº Baños:', home.baths)
    print('Tamaño:', home.size)
    print('Planta:', home.floor)

    # Characteristics
    
