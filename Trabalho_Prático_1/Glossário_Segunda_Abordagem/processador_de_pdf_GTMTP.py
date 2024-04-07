import re
import json

ficheiro = open("Glossário_de_Termos_Médicos_Técnicos_e_Populares.xml" ,encoding="utf-8")
texto = ficheiro.read()

texto = re.sub(r"<page(.)+>", r"", texto)
texto = re.sub(r"</page>", r"", texto)
texto = re.sub(r"<fontspec(.)+>", r"", texto)
texto = re.sub(r"<text(.)+\">", r"", texto)
texto = re.sub(r"</text>", r"", texto)
texto = re.sub(r"<b>[A-Z]</b>", r"", texto)
texto = re.sub(r"'blister'", r"blister", texto)
texto = re.sub(r"\(herpes\)", r"herpes", texto)
texto = re.sub(r"\(d\)", r"d", texto)

texto_list = texto.split("\n")

index = 0
for entry in texto_list:
    if entry == "" or entry == " " or entry == " , " or entry == "  ,  " or entry == " ,  " or entry == ", " or len(entry) == 1:
        texto_list[index] = "$"
    elif len(re.findall(r"\(pop\)", entry)) > 0:
        texto_list[index] = "SEPARADOR"
    index += 1

texto_list = [item for item in texto_list if item != "$"]

texto_dict = {}
index_1 = 0
while index_1 < len(texto_list):
    if len(texto_list) - index_1 > 4:
        if len(re.findall(r"<i>(.*?)</i>", texto_list[index_1])) > 0 and texto_list[index_1 + 1] == "SEPARADOR" and len(re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 2])) > 0 and len(re.findall(r"-</b>", texto_list[index_1 + 2])) > 0 and len(re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 3])) > 0:
            termo = re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 2])[0] + re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 3])[0]
            significado = re.findall(r"<i>(.*?)</i>", texto_list[index_1])[0]
            texto_dict[termo] = significado
            index_1 += 4
        elif len(re.findall(r"<i>(.*?)</i>", texto_list[index_1])) > 0 and texto_list[index_1 + 1] == "SEPARADOR" and len(re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 2])) > 0 and len(re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 3])) > 0 and len(re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 4])) > 0:
            termo = re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 2])[0] + re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 3])[0]
            significado = re.findall(r"<i>(.*?)</i>", texto_list[index_1])[0]
            texto_dict[termo] = significado
            index_1 += 4
        elif len(re.findall(r"<b>(.*?)</b>", texto_list[index_1])) > 0 and len(re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 1])) > 0 and texto_list[index_1 + 2] == "SEPARADOR":
            termo = re.findall(r"<b>(.*?)</b>", texto_list[index_1])[0]
            significado = re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 1])[0]
            texto_dict[termo] = significado
            index_1 += 3
        elif len(re.findall(r"<i>(.*?)</i>", texto_list[index_1])) > 0 and texto_list[index_1 + 1] == "SEPARADOR" and len(re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 2])) > 0:
            termo = re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 2])[0]
            significado = re.findall(r"<i>(.*?)</i>", texto_list[index_1])[0]
            texto_dict[termo] = significado
            index_1 += 3
        elif len(re.findall(r"<b>(.*?)</b>", texto_list[index_1])) > 0 and len(re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 1])) > 0 and len(re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 2])) > 0 and texto_list[index_1 + 3] == "SEPARADOR":
            termo = re.findall(r"<b>(.*?)</b>", texto_list[index_1])[0]
            significado = re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 1])[0] + re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 2])[0]
            texto_dict[termo] = significado
            index_1 += 4
        elif len(re.findall(r"<i>(.*?)</i>", texto_list[index_1])) > 0 and len(re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 1])) > 0 and texto_list[index_1 + 2] == "SEPARADOR" and len(re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 3])) > 0:
            termo = re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 3])[0]
            significado = re.findall(r"<i>(.*?)</i>", texto_list[index_1])[0] + re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 1])[0]
            texto_dict[termo] = significado
            index_1 += 4
        elif len(re.findall(r"<b>(.*?)</b>", texto_list[index_1])) > 0 and len(re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 1])) > 0 and len(re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 2])) > 0 and len(re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 3])) > 0 and texto_list[index_1 + 4] == "SEPARADOR":
            termo = re.findall(r"<b>(.*?)</b>", texto_list[index_1])[0]
            significado = re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 1])[0] + re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 2])[0] + re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 3])[0]
            texto_dict[termo] = significado
            index_1 += 5
        elif len(re.findall(r"<i>(.*?)</i>", texto_list[index_1])) > 0 and len(re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 1])) > 0 and len(re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 2])) > 0 and texto_list[index_1 + 3] == "SEPARADOR" and len(re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 4])) > 0:
            termo = re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 4])[0]
            significado = re.findall(r"<i>(.*?)</i>", texto_list[index_1])[0] + re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 1])[0] + re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 2])[0]
            texto_dict[termo] = significado
            index_1 += 5
        elif len(re.findall(r"<b>(.*?)</b>", texto_list[index_1])) > 0 and texto_list[index_1 + 1] == "SEPARADOR":
            termo = re.findall(r"<b>(.*?)</b>", texto_list[index_1])[0]
            significado = "N/A"
            texto_dict[termo] = significado
            index_1 += 2
        elif texto_list[index_1] == "SEPARADOR" and len(re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 1])) > 0:
            termo = re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 1])[0]
            significado = "N/A"
            texto_dict[termo] = significado
            index_1 += 2
    else:
        if len(re.findall(r"<b>(.*?)</b>", texto_list[index_1])) > 0 and len(re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 1])) > 0 and texto_list[index_1 + 2] == "SEPARADOR":
            termo = re.findall(r"<b>(.*?)</b>", texto_list[index_1])[0]
            significado = re.findall(r"<i>(.*?)</i>", texto_list[index_1 + 1])[0]
            texto_dict[termo] = significado
            index_1 += 3
        elif len(re.findall(r"<i>(.*?)</i>", texto_list[index_1])) > 0 and texto_list[index_1 + 1] == "SEPARADOR" and len(re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 2])) > 0:
            termo = re.findall(r"<b>(.*?)</b>", texto_list[index_1 + 2])[0]
            significado = re.findall(r"<i>(.*?)</i>", texto_list[index_1])[0]
            texto_dict[termo] = significado
            index_1 += 3

texto_dict_organizado = {}
chaves = sorted(texto_dict.keys())
for chave in chaves:
    texto_dict_organizado[chave] = texto_dict[chave]

file_out_siglas = open("texto.xml", "w")
file_out_siglas.write(texto)
file_out_siglas.close()

file_out_texto_dict = open("texto.json", "w", encoding="utf8")
json.dump(texto_dict_organizado,file_out_texto_dict, indent=4, ensure_ascii=False)
file_out_texto_dict.close()