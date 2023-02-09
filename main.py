import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

url ="https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil"
html = urlopen(url)

soup = BeautifulSoup(html, "html.parser")

padrao_estado=re.compile(" \([A-Z]{2}\)")

for linha in soup.find_all("li"):
    #print(linha)
    #if padrao_estado.search(linha):
        if padrao_estado.search(linha.text):
            print(linha.text)