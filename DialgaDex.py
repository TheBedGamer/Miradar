# DialgaDex - Top Rankings

import pandas as pd
from bs4 import BeautifulSoup
import requests

def rank(type):
    url = "https://www.dialgadex.com/?strongest=&t=" + type
    code = requests.get(url)
    soup = BeautifulSoup(code.text, 'html.parser')
    return soup.prettify()

print(rank("Water"))