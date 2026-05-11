import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

driver = webdriver.Chrome()

url = 'https://www.cnnbrasil.com.br/tudo-sobre/inteligencia-artificial/'

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

driver.implicitly_wait(10)

noticias = soup.find_all('figure')

dados = []
for noticia in noticias:
    titulo = noticia.find('h2', class_='text-xl font-bold').text.strip()
    link = noticia.find('a')['href']
    dados.append({'titulo': titulo, 'link': link})
    with open('noticias.json', 'w') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)



driver.quit()