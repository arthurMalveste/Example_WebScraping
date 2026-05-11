import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver

# Coloquei valores padrão (None) para as classes, assim elas se tornam opcionais
def webscraping(url, tag_dad, tag_sun, class_name_sun=None, class_name_dad=None):
    driver = webdriver.Chrome()
    driver.get(url)
    
    # 1. Espera a página renderizar de verdade antes de roubar o HTML
    time.sleep(4) 
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # 2. Busca o elemento "pai" com ou sem classe, dependendo do que foi passado
    if class_name_dad:
        noticias = soup.find_all(tag_dad, class_=class_name_dad)
    else:
        noticias = soup.find_all(tag_dad)
        
    dados = []
    
    for noticia in noticias:
        # 3. Busca o título e o link, mas não extrai o texto ainda
        if class_name_sun:
            elemento_titulo = noticia.find(tag_sun, class_=class_name_sun)
        else:
            elemento_titulo = noticia.find(tag_sun)
            
        elemento_link = noticia.find('a')
        
        # 4. Só extrai o dado se o título e o link realmente existirem naquele bloco
        if elemento_titulo and elemento_link:
            titulo = elemento_titulo.text.strip()
            link = elemento_link['href']
            dados.append({'titulo': titulo, 'link': link})
            
    # 5. Salva no JSON UMA ÚNICA VEZ, fora do loop
    with open('noticias.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
        
    driver.quit()
    print(f"Extração concluída! {len(dados)} notícias salvas.")

url1 = 'https://www.cnnbrasil.com.br/tudo-sobre/inteligencia-artificial/'

webscraping(
    url=url1, 
    tag_dad='figure', 
    tag_sun='h2', 
    class_name_sun='text-xl font-bold', 
    class_name_dad=None
)