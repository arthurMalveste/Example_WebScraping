import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()   

# 1. Configuração da "Senha" de acesso
genai.configure(api_key=os.getenv("gemini"))

def resumir_texto_com_ia(texto_da_noticia):
    # 2. Escolhendo qual "cérebro" vamos usar
    modelo = genai.GenerativeModel('gemini-1.5-flash')
    
    # 3. Engenharia de Prompt (A instrução clara)
    prompt = f"""
    Você é um assistente de pesquisa especializado na metodologia STAMP e em Inteligência Artificial.
    Leia o documento abaixo e faça um resumo executivo de no máximo 3 parágrafos focando nos 
    principais riscos, tecnologias envolvidas e inovações citadas.
    
    DOCUMENTO:
    {texto_da_noticia}
    """
    
    # 4. Enviando e aguardando a resposta
    resposta = modelo.generate_content(prompt)
    
    return resposta.text

