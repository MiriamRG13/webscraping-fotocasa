# Import libraries
import requests
from bs4 import BeautifulSoup
import csv
import time
import pandas as pd


# Global variables
url = 'https://www.fotocasa.es/es/comprar/vivienda/madrid-capital/aire-acondicionado-calefaccion-trastero-ascensor-internet-no-amueblado/157915887/d'
# time.sleep(30)


# Getting whole information (HTML) in page_url
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

# piso = [price, rooms, bath, size, floors]
piso = [None, None, None, None, None]
# Searching information
# Price
price = soup.find('span', attrs = { 'class':'re-DetailHeader-price' }).string
b = slice(len(price)-2)
piso[0] = price[b]

# Header
header = soup.findAll('li', attrs = { 'class': 're-DetailHeader-featuresItem'})
for i in header:
    element = i.findAll('span')
    tmp = element[len(element)-2].get_text().split(' ')
    number = tmp[0]
    if len(tmp) != 1:
        type = tmp[1]
        if type == 'habs.':
            piso[1] = number
        if type == 'baños':
            piso[2] = number
        if type.startswith('m'):
            piso[3] = number
        if type == 'Planta':
            a = slice(len(number)-1)
            piso[4] = number[a]
    else:
        number = element[len(element)-1].get_text()


print('Precio:', piso[0])
print('Nº Habitaciones:', piso[1])
print('Nº Baños:', piso[2])
print('Tamaño:', piso[3])
print('Planta:', piso[4])


# Characteristics
       
