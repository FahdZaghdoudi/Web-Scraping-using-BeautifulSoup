# Load the packages required
import requests
from bs4 import BeautifulSoup

# Defining the url of the site
base_site = "https://www.babnet.net/"

# Making a get request
response = requests.get(base_site)
#response.status_code : if 200 the everything is OK

# Extracting the HTML
html = response.content

# Convert HTML to a BeautifulSoup object. This will allow us to parse out content from the HTML more easily.
# Using the default parser as it is included in Python
soup = BeautifulSoup(html, "html.parser")

# Searching and navigating the HTML tree
x1 = soup.find_all('h2', class_ = 'post-title arabi')
x2 = soup.find_all('h2', class_ = 'post-title title-medium arabi')
x3 = soup.find_all('h2', class_ = 'post-title title-small arabi')
x4 = x1 + x2 + x3
# Create e beautifulsoup object from our list 
aa = BeautifulSoup(str(x4), "html.parser")

# Extract all links 
links = aa.find_all('a')

# We obtained relative URLs
# To obtain the absolute URL address we will use urljoin
from urllib.parse import urljoin
relative_urls = [link.get('href') for link in links]

# Transforming to absolute path URLs
full_urls = [urljoin(base_site, url) for url in relative_urls]

#to avoid limiting the number of requests, we should tellpython to wait between each request
#we importtime library
import time
# initialize lists to store titles, types and articles for each webpage
article = []
titles = []
types = []

# creating a loop counter
i = 0

print('-------------------------- Beginning of Scraping --------------------------')

# Loop through each URL in note_urls
for url in full_urls:
    
    #wait 1 seconde between requests
    #time.sleep(1)
    
    # connect to every webpage
    note_resp = requests.get(url)
    
    
    # checking if the request is successful
    if note_resp.status_code == 200:            # Everything is OK!
        print('URL #{0}: {1}'.format(i+1,url))    # print out the number of iteration and the URL to keep track of place in loop
    
    else:                                       # Something is wrong!
        print('Status code {0}: Skipping URL #{1}: {2}'.format(note_resp.status_code, i+1, url))
        i = i+1
        continue
        
    
    # get HTML from webpage
    note_html = note_resp.content
    
    # convert HTML to BeautifulSoup object
    note_soup = BeautifulSoup(note_html, 'lxml')
    
    # Removing ads from our pages
    for div in note_soup.find_all("div", {'class':'noprint'}): 
        div.decompose()
        
    # Removing source text
    for src in note_soup.find_all("span", {'class':'source'}): 
        src.decompose()
    
    # find  articles on the webpage
    note_pars = note_soup.find_all('div' , class_ = 'entry-content arabi')
    
    # find the title
    note_titles = note_soup.find_all('h2' , class_ = 'post-title arabi')
    
    # find types
    note_types = note_soup.find_all('li' , class_ = 'nav-item active')
    
    
    # Transforming to text and cleaning every desired element in the page
    art = [(p.text).replace('\n','').replace('\t','').replace('\r','') for p in note_pars]
    tit = [(t.text).replace('\n','').replace('\t','').replace('\r','') for t in note_titles]
    typ = [(ty.text).replace('\n','').replace('\t','').replace('\r','') for ty in note_types]
    
    # Append to our lists
    article.append(str(art)[2:-2])
    titles.append(str(tit)[2:-2])
    types.append(str(typ)[2:-2])
    
    # Incrementing the loop counter
    i = i+1
    
print('-------------------------- SCRAPING DONE --------------------------')


# Import pandas to create our dataframe 
import pandas as pd
# Create a dataframe with our scraped data
df = pd.DataFrame(list(zip(full_urls, titles, article, types)), columns =['link', 'titles', 'article', 'type']) 
# Create and download the csv file
path = ('C:/Users/FAHD/Desktop/Formation/Web Scraping/AI Squad/BabNet/BabNett.csv')
df.to_csv(path, encoding='utf-8-sig')




























