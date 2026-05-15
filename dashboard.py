import streamlit as st
import json

st.set_page_config(page_title="Base de Dados STAMP", layout="centered")

# 2. Cabeçalho da sua página
st.title("📰 Base de Dados - Notícias IA")
st.write("Estes são os documentos capturados pelo nosso Web Crawler para análise futura.")
st.divider() # Cria uma linha horizontal para separar

# 3. Lendo o arquivo JSON que o seu Crawler gerou
try:
    with open('noticias.json', 'r', encoding='utf-8') as f:
        noticias = json.load(f)
except FileNotFoundError:
    st.error("Arquivo noticias.json não encontrado. Rode o Crawler primeiro!")
    noticias = []

# 4. Desenhando cada notícia na tela
for noticia in noticias:
    # Mostra o título
    st.subheader(noticia.get('titulo', 'Título não encontrado'))
    
    # Mostra o link clicável
    link = noticia.get('link', '#')
    st.markdown(f"🔗 [Acessar documento original]({link})")
    
    # Cria uma caixa sanfonada para o conteúdo gigante não poluir a tela
    with st.expander("Ler texto extraído"):
        texto = noticia.get('conteudo', 'Sem conteúdo')
        # O st.write entende textos longos e faz a quebra de linha certinha
        st.write(texto)
    
    # Espaçamento extra entre uma notícia e outra
    st.write("")