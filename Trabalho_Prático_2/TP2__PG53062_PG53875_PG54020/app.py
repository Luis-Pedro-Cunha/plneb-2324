from flask import Flask, render_template, request, redirect
import json
import re
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)

file = open("dic_novo.json", "r", encoding="utf-8")
termos = json.load(file)
file.close()

file_traduc = open("novo_PT_EN.json", "r", encoding="utf-8")
traduc = json.load(file_traduc)
file_traduc.close()

file_gloss = open("glossario.json", "r", encoding="utf-8")
gloss = json.load(file_gloss)
file_gloss.close()

file_popular = open("texto.json", encoding="utf-8")
popular = json.load(file_popular)
file_popular.close()

traduc_keys = list(traduc.keys())
gloss_keys = list(gloss.keys())
pop_keys = list(popular.keys())
all_keys = list(set(traduc_keys + gloss_keys + pop_keys))

global_dicti = {}
for key in all_keys:
    global_dicti[key] = {}
    if key in traduc_keys:
        global_dicti[key]['traduc'] = traduc[key]
    else:
        global_dicti[key]['traduc'] = None
    if key in gloss_keys:
        global_dicti[key]['desc'] = gloss[key]['desc']
        global_dicti[key]['sinon'] = gloss[key]['sinonimos']
    else:
        global_dicti[key]['desc'] = None
        global_dicti[key]['sinon'] = None
    if key in pop_keys:
        global_dicti[key]['pop'] = popular[key]
    else:
        global_dicti[key]['pop'] = None

teste = open("teste.json", "w", encoding="utf-8")
json.dump(global_dicti, teste, indent=4, ensure_ascii=False)
teste.close()

file_siglas = open("siglas.json", encoding="utf-8")
siglas = json.load(file_siglas)
file_siglas.close()

sig_keys = list(siglas.keys())

categorias = []
for elem in termos.values():
    if ";" in elem["categoria"]:
        categs = elem["categoria"].split(";")
        for c in categs:
            categorias.append(c)
    else:
        categorias.append(elem["categoria"])

categorias = list(set(categorias))
categorias = sorted(categorias)
categorias.remove("Outro")
categorias.append("Outro")

def guardar_termos(termos):
    with open("dic_novo.json", "w", encoding="utf-8") as file:
        json.dump(termos, file, ensure_ascii=False, indent=4)

@app.route("/")
def home():
    return render_template("home.html", title='HOME', categorias = categorias)

@app.route("/<string:categoria>")
def termos_categoria(categoria):
    categoria = re.sub(r"%20"," ",categoria)
    termos_keys = list(termos.keys())
    termos_cat = []
    for key in termos_keys:
        if categoria in termos[key]['categoria']:
            termos_cat.append(key)
    return render_template("categoria.html", title=categoria, termos_cat=termos_cat, categorias=categorias)

@app.route("/conceito/<string:termo>")
def termo_info(termo):
    termo = re.sub(r"%20", " ", termo)
    if termo in termos.keys():
        lista_t = termo.split()
        if len(lista_t) == 1:
            url = f"https://pubmed.ncbi.nlm.nih.gov/?term={termo}"
        else:
            t=""
            for j in range(len(lista_t)):
                if j == 0:
                    t+=lista_t[j]
                else:
                    t+="+"+lista_t[j]
            url = f"https://pubmed.ncbi.nlm.nih.gov/?term={t}"
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        artigos = soup.find_all("a", class_="docsum-title")
        artigos_termo = {}
        for elem in artigos:
            if elem != None:
                ref = elem["href"]  # Obtendo o link do artigo
                refer = f"https://pubmed.ncbi.nlm.nih.gov{ref}"
                nome = elem.text.strip()
                artigos_termo[nome] = refer
        validation = False
        for objeto in gloss.keys():
            if objeto in termos[termo]["descricao"]:
                if gloss[objeto]["artigos relacionados"] != None:
                    validation = True
        return render_template("conceito.html", title=termo, conceito_info=termos[termo], validation=validation, categorias=categorias, glossario=gloss, global_dicti=global_dicti, termos=termos, google_url=google_url, art_pubmed=artigos_termo)
    else:
        mensagem = f"O conceito {termo} não existe no dicionário."
        return render_template("erro.html", mensagem=mensagem)

@app.route("/Conceitos")
def conceitos():
    search_query = request.args.get('search')
    if search_query:
        resultados = {key: value for key, value in termos.items() if search_query.lower() in key.lower() or search_query.lower() in value['descricao'].lower()}
        num_resultados = len(resultados)
        mensagem = f"Foram encontrados {num_resultados} resultados da pesquisa por '{search_query}'."
        return render_template("Conceitos.html", conceitos=resultados, categorias=categorias, mensagem=mensagem)
    else:
        mensagem = ""
        return render_template("Conceitos.html", conceitos=termos, categorias=categorias, mensagem=mensagem)

@app.route("/Conceitos", methods = ["POST"])
def adicionar_conceitos():
    termo = request.form.get("termo")
    descricao = request.form.get("descricao")
    categoria = request.form.get("categoria")
    if termo in termos:
        mensagem = f"O termo '{termo}' já existe no dicionário e não pode ser adicionado novamente."
        return render_template("Conceitos.html", conceitos=termos, categorias=categorias, mensagem=mensagem)
    elif termo == "":
        mensagem = f"Não pode adicionar um termo vazio."
        return render_template("Conceitos.html", conceitos=termos, categorias=categorias, mensagem=mensagem)
    else:
        termos[termo] = {"categoria":categoria,"descricao": descricao, "siglas" : {}}
        for sig in sig_keys:
            if sig in termo or sig in termos[termo]["descricao"]:
                termos[termo]["siglas"][sig] = siglas[sig]
        guardar_termos(termos)
        mensagem = f"O termo '{termo}' foi adicionado com sucesso!"
        return render_template("Conceitos.html", conceitos = termos, categorias=categorias, mensagem= mensagem)

@app.route('/google/<string:termo>')
def google_url(termo):
    url = google_url(termo)
    return redirect(url)

@app.route("/excluir_conceito/<string:termo>", methods=["POST"])
def excluir_conceito(termo):
    if termo in termos:
        del termos[termo]
        guardar_termos(termos)
        mensagem = f"O conceito '{termo}' foi excluído com sucesso!"
    else:
        mensagem = f"O conceito '{termo}' não foi encontrado no dicionário e não pôde ser excluído."
    return render_template("Conceitos.html", conceitos=termos, categorias=categorias, mensagem=mensagem)

@app.route("/editar_conceito/<string:termo>")
def editar_conceito_pagina(termo):
    if termo in termos:
        return render_template("editar_conceito.html", title=termo, conceito_info=termos[termo], categorias=categorias)
    else:
        mensagem = f"O conceito '{termo}' não foi encontrado no dicionário."
        return render_template("erro.html", categorias=categorias, mensagem=mensagem)

@app.route("/editar_conceito/<string:termo>", methods=["POST"])
def editar_conceito(termo):
    nova_descricao = request.form.get("nova_descricao")
    if termo in termos:
        termos[termo]["descricao"] = nova_descricao
        guardar_termos(termos)
    termo = re.sub(r"%20", " ", termo)
    if termo in termos.keys():
        lista_t = termo.split()
        if len(lista_t) == 1:
            url = f"https://pubmed.ncbi.nlm.nih.gov/?term={termo}"
        else:
            t = ""
            for j in range(len(lista_t)):
                if j == 0:
                    t += lista_t[j]
                else:
                    t += "+" + lista_t[j]
            url = f"https://pubmed.ncbi.nlm.nih.gov/?term={t}"
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        artigos = soup.find_all("a", class_="docsum-title")
        artigos_termo = {}
        for elem in artigos:
            if elem != None:
                ref = elem["href"]  # Obtendo o link do artigo
                refer = f"https://pubmed.ncbi.nlm.nih.gov{ref}"
                nome = elem.text.strip()
                artigos_termo[nome] = refer
        validation = False
        for objeto in gloss.keys():
            if objeto in termos[termo]["descricao"]:
                if gloss[objeto]["artigos relacionados"] != None:
                    validation = True

        return render_template("conceito.html", title=termo, conceito_info=termos[termo], validation=validation, categorias=categorias, glossario=gloss, global_dicti=global_dicti, termos=termos, google_url=google_url, art_pubmed=artigos_termo)
    else:
        mensagem = f"O conceito '{termo}' não foi encontrado no dicionário."
        return render_template("erro.html", mensagem=mensagem)

def google_url(termo):
    query = quote_plus(termo)
    url = f"https://www.google.com/search?q={query}"
    return url

app.run(host="localhost", port=5000, debug=True)
