import re
import json

file = open("Glossário de Termos Médicos Técnicos e Populares.xml", encoding="utf-8")
texto = file.read()

#LIMPEZA DO CONTEÚDO
texto = re.sub(r'<text.+font="4".+</text>', r'', texto)
texto = re.sub(r'<page.+number.+>', r'', texto)
texto = re.sub(r"<text[^<]*", r"", texto)
texto = re.sub(r"</text>", r"", texto)
texto = re.sub(r"</page>", r"", texto)
texto = re.sub(r"<fontspec.*?>", r"", texto)
texto = re.sub(r"&#34;", r"", texto)
texto = re.sub(r'\n<i>',r'<i>',texto)
texto = re.sub(r'\n<b>',r'<b>',texto)
texto = re.sub(r'</i><i>',r' ',texto)
texto = re.sub(r'</b><b>',r' ',texto)
texto = re.sub(r'\n\s*\n', r'\n',texto)
texto = re.sub(r'</b><i>', r'</b>\n<i>',texto)

with open('novo_xml.xml','w',encoding='utf-8') as file:
    file.write(texto)


#EXTRAÇÃO DOS TERMOS
pop = re.findall(r'<i>(.*)</i>',texto)
termos = re.findall(r'<b>(.*)</b>',texto)

#CRIAÇÃO DO DICIONÁRIO
conceitos_dict = {}
a=0
b=0
while a < (len(termos)) and b < (len(pop)):
    if termos[a] not in conceitos_dict.keys():
        conceitos_dict[termos[a]] = pop[b]
    a+=1
    b+=1


#CRIAÇÃO DO FICHEIRO JSON
glossario = open("glossário.json","w", encoding = "utf-8")
json.dump(conceitos_dict, glossario, indent=4, ensure_ascii=False)
glossario.close()