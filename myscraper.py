# after python install, pip install these 2 libraries from the command prompt
# while online then import as shown

import requests
from bs4 import BeautifulSoup
import pandas as pd

# bring desired webpage into python and create soup object via beautifulsoup

url = 'https://pauladeen.com/recipe/mashed-potatoes-with-sautaed-mushrooms/'
# url = 'https://pauladeen.com/recipe/fried-bacon-mashed-potatoes/'
# url = 'https://pauladeen.com/recipe/shrimp-mashed-potatoes/'
r = requests.get(url)

# different parsers for different websites and output, these are the main ones
soup = BeautifulSoup(r.text, 'html.parser')

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

# print to see what I've got
print(soup.find('title').text)

# url of image
pic = soup.find('img', class_='img-fluid').get('data-src')

# print to see what I've got
print(pic)

records.append(pic)
records.append(' ')

# list of ingredients
ingredients = []
for results1 in soup.find_all('li', itemprop='ingredients'):
    # print to see what I've got
    print(results1.text)

    ingredients.append(results1.text)
    records.append(results1.text)
records.append(' ')

# list of instructions
directions = []
for results in soup.find_all('p'):
    # print to see what I've got
    print(results.text)

    directions.append(results.text)
    records.append(results.text)
records.append(' ')

# create data frame object out of records
df = pd.DataFrame(records)
records

# send to folder of source file as .csv file, open with spreadsheet app(excel)
df.to_csv('pdRecipies.csv', index=False, encoding='utf-8')
