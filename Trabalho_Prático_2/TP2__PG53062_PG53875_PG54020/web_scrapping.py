import requests
from bs4 import BeautifulSoup
import json
import re

url = "https://www.mdsaude.com/glossario/"

def get_content(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    conteudo = soup.find_all("div", class_="kt-tab-inner-content-inner")
    separacao_por_termo = []
    for conteudo_letra in conteudo:
        partes = str(conteudo_letra).split('<hr class="wp-block-separator has-alpha-channel-opacity"/>')
        for parte in partes:
            conteudo_termo=parte.split("\n")
            lista_indices = []
            if "" in conteudo_termo:
                conteudo_termo.remove("")
            if "<div class=\"kt-tab-inner-content-inner\">" in conteudo_termo:
                conteudo_termo.remove("<div class=\"kt-tab-inner-content-inner\">")
            if "<ul>" in conteudo_termo:
                conteudo_termo.remove("<ul>")
            if "</ul>" in conteudo_termo:
                conteudo_termo.remove("</ul>")
            if "</div>" in conteudo_termo:
                conteudo_termo.remove("</div>")
            if "" in conteudo_termo:
                conteudo_termo.remove("")
            if "<ol>" in conteudo_termo:
                conteudo_termo.remove("<ol>")
            if "</ol>" in conteudo_termo:
                conteudo_termo.remove("</ol>")
            separacao_por_termo.append(conteudo_termo)
    dicionario = {}
    for item in separacao_por_termo:
        termo = None
        descricao = None
        sinonimos = None
        artigos = None

        for elemento in item:
            elemento = re.sub(r"\xa0", "", elemento)
            elemento = re.sub("Sinônimos: ", "", elemento)
            soup = BeautifulSoup(elemento, "html.parser")
            if soup.find("strong"):
                termo = soup.find("strong").text
            elif soup.find("a"):
                artigos = soup.find("a")["href"]
            elif soup.find("p"):
                descricao = soup.find("p").text
                if '₂' in descricao:
                    descricao = re.sub(r'₂', '2', descricao)
            elif soup.find("li"):
                sinonimos = soup.find("li").text
        if termo != None:
            dicionario[termo.lower()] = {"desc": descricao, "sinonimos": sinonimos, "artigos relacionados": artigos}
    return dicionario

dicionario = get_content(url)

glossario = open("glossario.json", "w", encoding="utf-8")
json.dump(dicionario, glossario, indent=4, ensure_ascii=False)
glossario.close()