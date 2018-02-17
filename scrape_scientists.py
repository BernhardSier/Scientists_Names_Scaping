# Scape the enitre list of scientists from 'https://www.famousscientists.org/list/'
import requests
from bs4 import BeautifulSoup

# Get site content
url = 'https://www.famousscientists.org/list/'
page = requests.get(url)

# Get soup
soup = BeautifulSoup(page.content, 'html.parser')

# Scrape Names from each of the 3 columns
names =  soup.find('div',{'class':'list_coly_1'})
names.append(soup.find('div',{'class':'list_coly_2'}))
names.append(soup.find('div',{'class':'list_coly_3'}))
names = names.findAll('a')

# Save each name to a file
open_file = open('famous_scientists.txt', 'w')
for i in range(0,len(names)):
    open_file.write(names[i].contents[0] + '\n')
open_file.close()

print("This script has finished. Goodbye.")