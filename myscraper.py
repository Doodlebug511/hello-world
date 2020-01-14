
#after python install, pip install these 2 libraries from the command prompt while online
#then import as shown
import requests
from bs4 import BeautifulSoup

#bring desired webpage into python and create soup object via beautifulsoup
r = requests.get('https://pauladeen.com/recipe/mashed-potatoes-with-sautaed-mushrooms/')
#r = requests.get('https://pauladeen.com/recipe/fried-bacon-mashed-potatoes/')
#r = requests.get('https://pauladeen.com/recipe/shrimp-mashed-potatoes/')

#different parsers for different websites and output, these are the main ones
soup = BeautifulSoup(r.text, 'html.parser')
#soup = BeautifulSoup(r.text, 'lxml.parser') #will need a pip install of lxml first
#soup = BeautifulSoup(r.text, 'html5lib.parser') #pip install of html5lib first

records = []  #main container for soup object

records.append(soup.find('title').text) #adding title text to records array
records.append(' ')                     #adding spacer between texts for readability 
print(soup.find('title').text)          #print to see what I've got

pic = soup.find('img', class_='img-fluid').get('data-src')  #url of image
print(pic)
records.append(pic)
records.append(' ')

ingredients = []
for results1 in soup.find_all('li', itemprop='ingredients'): #list of ingredients
    print(results1.text)
    ingredients.append(results1.text)
    records.append(results1.text)
records.append(' ')    

directions = []
for results in soup.find_all('p'):  #list of instructions
    print(results.text)
    directions.append(results.text)
    records.append(results.text)
records.append(' ')    

#pip install pandas, then import
import pandas as pd

df = pd.DataFrame(records)  #create data frame object out of records
records
#send to folder of source file as .csv file, open with spreadsheet app(excel)
df.to_csv('pdRecipies.csv', index = False, encoding='utf-8') 



