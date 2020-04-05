#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as bs

# GoodRx `Where Can I Get a Drive-Thru Coronavirus (Covid-19) Test Near Me?`
# embeded table url
data_url = 'https://datawrapper.dwcdn.net/H7PJn/6/'

site_data = requests.get(data_url)

soup = bs(site_data.text, 'html.parser')

# Parse javascript function containing drive thru location data
raw_table = soup.find_all('script')[-1]

print(str(raw_table))
