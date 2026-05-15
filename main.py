import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver


def webscraping(url, tag_dad, tag_son, class_name_son=None, class_name_dad=None):
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
        if class_name_son:
            elemento_titulo = noticia.find(tag_son, class_=class_name_son)
        else:
            elemento_titulo = noticia.find(tag_son)
            
        elemento_link = noticia.find('a')
        
        # 4. Só extrai o dado se o título e o link realmente existirem
        if elemento_titulo and elemento_link:
            titulo = elemento_titulo.text.strip()
            link = elemento_link['href']
            
            # Navega para a página interna
            driver.get(link)
            time.sleep(2) 
            
            # Nova sopa para a página interna
            soup_interna = BeautifulSoup(driver.page_source, 'html.parser')
            conteudo_all = soup_interna.find('div', class_='text-lg w-full pt-6 font-light text-neutral-800 group-[.isActiveSource>*]:text-xl md:pt-10 [&>*:not(.single-product)]:mx-auto [&>*:not(.single-product)]:max-w-2xl [&_.gallery]:mb-4 [&_p]:my-4 first:[&_p]:mt-0 [&_strong]:font-medium')
            
            if conteudo_all:
                # Pega TODOS os parágrafos e junta em um texto só
                paragrafos = conteudo_all.find_all('p', class_='my-5 break-words group-[.isActiveSource]:text-xl')
                texto_materia = " ".join([p.text.strip() for p in paragrafos])
            else:
                texto_materia = 'Conteúdo não encontrado'
            
            # Adiciona tudo de uma vez ao dicionário
            dados.append({
                'titulo': titulo, 
                'link': link,
                'conteudo': texto_materia
            })

            
    # 5. Salva no JSON UMA ÚNICA VEZ, fora do loop
    with open('noticias.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
        
    driver.quit()
    print(f"Extração concluída! {len(dados)} notícias salvas.")

url1 = 'https://www.cnnbrasil.com.br/tudo-sobre/inteligencia-artificial/'

webscraping(
    url=url1, 
    tag_dad='figure', 
    tag_son='h2', 
    class_name_son='text-xl font-bold', 
    class_name_dad=None
)



# -----------------------------------Config para o site da EXAME-----------------------------------

# url2 = 'https://exame.com/inteligencia-artificial/'
# webscraping(
#     url=url2, 
#     tag_dad='div', 
#     tag_son='h3', 
#     class_name_son='m-0 p-0 xl:text-pretty headline-extra-small text-colors-text', 
#     class_name_dad='sc-c7f3f647-9 cSIPEY election_undefined'
# )

#-----------------------------------------------------------------------




