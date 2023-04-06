#import libaries 
import requests
from bs4 import BeautifulSoup
import pandas as pd


#create a url obj
url = 'https://www.fxstreet.com/economic-calendar'
#create page response obj
page = requests.get(url)

print(page)
