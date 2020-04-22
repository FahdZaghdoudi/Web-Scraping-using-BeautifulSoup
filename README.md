# Web-Scraping-using-BeautifulSoup

The need and importance of extracting data from the web is becoming increasingly loud and clear.
For some <b>Artificial Intelligence projects</b>, I find myself in a situation where I need to extract data from the web.

This repo contains some scripts to extract data from Tunisian Websites for News using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) in [Python](https://www.python.org/).

## Scraping rules :
* Check a website's Term and Conditions before scraping it and read the statements about legal use of the data. 
* Do not request data from the website too aggressiely and ensure that your program behaves in a reasonable manner.

## Usage
* You can download and open the <b>python file</b> on your preferred editor.
* You can download and open the <b>notebook</b> on Jupyter Notebook or [Google Colab](https://colab.research.google.com/).

## Workflow
1. Insect the page
2. Obtain HTML
3. Choose a parser (lxml , html5lib , html.parser)
4. Create a beautifulsoup object
5. Extract tags that we need
6. Store the data in lists
7. Make a dataframe
8. Download a CSV file that contains all data scraped

## Specification
The scrapers are different between one site and another. So, to use those scrapers, you have to change the value of <i>base_site</i> with the url desired, and identify tags to extract.

## Packages used
```python
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import time
import pandas as pd
```

## Contributing
Pull requests are always welcome. For major changes, please contact me on my LinkedIn account [Fahd Zaghdoudi](https://www.linkedin.com/in/fahdzaghdoudi/)
