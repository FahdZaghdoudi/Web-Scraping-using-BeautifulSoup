# Load the packages required
import requests
from bs4 import BeautifulSoup

# Defining the url of the site
base_site = "http://www.assabahnews.tn/"

# Making a get request
response = requests.get(base_site)
#response.status_code : if 200 the everything is OK

# Extracting the HTML
html = response.content

# Using the default parser as it is included in Python
soup = BeautifulSoup(html, "html.parser")

# Removing videos section from our page
videos = soup.find("section", {'id':'block-views-op-recent-content-block-18'})
videos.decompose()

# Searching and navigating the HTML tree
x1 = soup.find_all('div', class_ = 'views-content-title')
x2 = soup.find_all('span', class_ = 'field-content')
x3 = x1 + x2
# Create e beautifulsoup object from our list 
aa = BeautifulSoup(str(x3), "html.parser")

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
# initialize lists to store titles and articles for each webpage
article = []
titles = []
types = []

# creating a loop counter
i = 0

# Loop through each URL in note_urls
for url in full_urls:
    #wait 1 second between requests
    time.sleep(1)
    
    # connect to every webpage
    note_resp = requests.get(url)
    
    # checking if the request is successful
    if note_resp.status_code != 200:
        print('Status code {0}: Skipping URL #{1}: {2}'.format(note_resp.status_code, i+1, url))
        i = i+1
        continue
        
    # get HTML from webpage
    note_html = note_resp.content
    
    # convert HTML to BeautifulSoup object
    note_soup = BeautifulSoup(note_html, 'lxml')

    # find  articles on the webpage
    note_pars = note_soup.find_all('div' , class_ = 'field-item even')
    
    # find the title
    note_titles = note_soup.find('h1' , id = 'page-title')
    
    # Transforming to text and cleaning every desired element in the page
    art = [(p.text).replace('\n','').replace('\t','').replace("\'",'') for p in note_pars]
    tit = [(t.string).replace('\n','').replace('\t','').replace('\r','') for t in note_titles]
    
    # Append to our lists
    article.append(str(art)[2:-2])
    titles.append(str(tit)[2:-2])
    types.append('nan')
    
    # Incrementing the loop counter
    i = i+1
    
print('-------------------------- SCRAPING DONE --------------------------')

# Import pandas to create our dataframe 
import pandas as pd
# Create a dataframe with our scraped data
df = pd.DataFrame(list(zip(full_urls, titles, article, types)), columns =['link', 'titles', 'article', 'type']) 
# Create and download the csv file
path = ('AssabahNews.csv')
df.to_csv(path, encoding='utf-8-sig')
