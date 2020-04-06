#!/usr/bin/env python3

import requests
import re
from os.path import join
from bs4 import BeautifulSoup as bs

# GoodRx `Where Can I Get a Drive-Thru Coronavirus (Covid-19) Test Near Me?`
# embeded table url
base_url = 'https://datawrapper.dwcdn.net/'
search_url = 'https://datawrapper.dwcdn.net/H7PJn/'

pre_scrape = requests.get(search_url)

soup = bs(pre_scrape.text, 'html.parser')

table_location_suffix = re.search('/H7PJn.*', soup.find('meta').attrs['content']).group().lstrip('/')

url = join(base_url, table_location_suffix)

res = requests.get(url)

soup = bs(res.text, 'html.parser')

# Parse javascript function containing drive thru location data
raw_table = soup.find_all('script')[-1]

print(str(raw_table))
