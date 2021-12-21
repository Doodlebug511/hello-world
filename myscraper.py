# basic web page scraper as final project for bootcamp...
# import needed modules

import requests
from bs4 import BeautifulSoup
import pandas as pd

# bring desired webpage into python and create soup object via beautifulsoup

url = 'https://pauladeen.com/recipe/mashed-potatoes-with-sautaed-mushrooms/'
# url = 'https://pauladeen.com/recipe/hash-brown-quiche/'
# url = 'https://pauladeen.com/recipe/paulas-sugared-rose-parade-layer-cake/'
r = requests.get(url)

# parse website into soup object
soup = BeautifulSoup(r.text, 'html.parser')

# different parsers for different websites and output, these are the main ones
# soup = BeautifulSoup(r.text, 'lxml.parser')
# will need a pip install of lxml first

# soup = BeautifulSoup(r.text, 'html5lib.parser')
# pip install of html5lib first

# main container for soup object
records = []

# adding title text to records array
records.append(soup.find('title').text)

# adding spacer between texts for readability
records.append(' ')

print(soup.find('title').text)
print()

# for title of saved csv file
recipe_title = soup.find('title').text
recipe_title = str(recipe_title) + '.csv'
recipe_title = recipe_title.replace('|', '-')

# url of recipe image from soup object
pic = soup.find('img', class_='img-fluid').get('data-src')

# add url of recipe image to main container
records.append('Picture of finished dish...')
records.append(pic)
records.append(' ')

print('Picture of finished dish...')
print(pic)
print()

# create list of ingredients from soup object, add to container
records.append('Ingredients...')
ingredients = []
for results1 in soup.find_all('li', itemprop='ingredients'):
    ingredients.append(results1.text)
    records.append(results1.text)

records.append(' ')

print('Ingredients...')
for item in ingredients:
    print(item)
print()

# create list of instructions from soup object, add to container
records.append('Directions...')
directions = []
for results in soup.find_all('p'):
    directions.append(results.text)
    records.append(results.text)

records.append(' ')

print('Directions...')
for item in directions:
    print(item)
print()

# create data frame object out of records
df = pd.DataFrame(records)

# send to folder of source file as .csv file, open with spreadsheet app(excel)
df.to_csv(recipe_title, index=False, encoding='utf-8')
