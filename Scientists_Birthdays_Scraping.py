# Import wikipedia and Beautiful Soup Modules
import wikipedia
from bs4 import BeautifulSoup
import pandas as pd
import os
import googlemaps


# Read in famous scientists name from file
try:
    with open('famous_scientists.txt', 'r') as open_file:
        names = open_file.read()
        names = names.split('\n')
except FileNotFoundError:
    print("Error: File does not exist\n")
    names = []

data = []
# Scape information from wikipedia
for i in range(0,5):#len(names)):
    # Create html soup
    page = wikipedia.page(names[i])
    soup = BeautifulSoup(page.html(),'html.parser')

    # Get data for entry
    try:
        _birth_date =  soup.find('span',{'class':'bday'})
        _bith_place =  soup.find('span',{'class':'birthplace'})
        _death_date =  soup.find('span',{'class':'dday deathdate'})
        data.append((names[i],_birth_date.text,_death_date.text,_bith_place.text))
    except (AttributeError, wikipedia.exceptions.DisambiguationError):
        print(str(i+1) + "    " + names[i])


labels = ['Name','Birth Date','Death Date', 'Birth Place']
df = pd.DataFrame.from_records(data,columns=labels)

print("The program has finished. Goodbye.")