import re
import json

ficheiro = open("glossario_ministerio_saude.xml" ,encoding="utf-8")
texto = ficheiro.read()
siglas = texto.split("$$$\n")[0]
dicionario = texto.split("$$$\n")[1]

siglas = re.sub(r"<page(.)+>", r"", siglas)
siglas = re.sub(r"</page>", r"", siglas)
siglas = re.sub(r"<fontspec(.)+>", r"", siglas)
siglas = re.sub(r"<b>Siglas</b>", r"", siglas)
siglas = re.sub(r"<text(.)+\">", r"", siglas)
siglas = re.sub(r"</text>", r"", siglas)
siglas = re.sub(r"\d", r"", siglas)
siglas = re.sub(r"\n", r"", siglas)
siglas = re.sub(r"\s?–\s?", r"", siglas)
siglas = re.sub(r"\s<", r"<", siglas)
siglas = re.sub(r">\s", r">", siglas)
siglas = re.sub(r"ﬁ\s", r"fi", siglas)
siglas = re.sub(r"ü", r"u", siglas)
siglas_termos = re.findall(r"<b>(.*?)</b>", siglas)
siglas_descr = re.findall(r"</b>(.*?)<b>|</b>(.*?)$", siglas)

siglas_dict = {}
j = 0
for i in siglas_termos:
    if siglas_descr[j][0] != "":
        siglas_dict[i] = siglas_descr[j][0]
    else:
        siglas_dict[i] = siglas_descr[j][1]
    j+=1

dicionario = re.sub(r"-</text>", r"</text>", dicionario)
dicionario = re.sub(r"-</b>", r"</b>", dicionario)
dicionario = re.sub(r"<image(.)+>", r"$", dicionario)
dicionario = re.sub(r"<page(.)+>", r"$", dicionario)
dicionario = re.sub(r"</page>", r"$", dicionario)
dicionario = re.sub(r"\t<fontspec(.)+>", r"$", dicionario)
dicionario = re.sub(r"ﬁ\s", r"fi", dicionario)
dicionario = re.sub(r"ü", r"u", dicionario)
dicionario = re.sub(r"<b>epidemiologia</b>", r"epidemiologia", dicionario)

dicionario_list = dicionario.split("\n")
index = 0
for entry in dicionario_list:
    if len(re.findall(r"font=\"22\"", entry)) > 0:
        dicionario_list[index] = "$"
    elif len(re.findall(r"font=\"23\"", entry)) > 0:
        dicionario_list[index] = "$"
    elif len(re.findall(r"font=\"25\"", entry)) > 0:
        dicionario_list[index] = "$"
    elif len(re.findall(r"font=\"24\"", entry)) > 0:
        dicionario_list[index] = "$"
    elif len(re.findall(r"top=\"238\"", entry)) > 0:
        dicionario_list[index] = "$"
    elif len(re.findall(r"top=\"234\"", entry)) > 0:
        dicionario_list[index] = "$"
    elif len(re.findall(r"top=\"233\"", entry)) > 0:
        dicionario_list[index] = "$"
    elif len(re.findall(r">\d+<", entry)) > 0:
        dicionario_list[index] = "$"
    index += 1

dicionario_list = [item for item in dicionario_list if item != "$"]

dicionario_termos = []
dicionario_catego = []
dicionario_descr = []
token_catego = 0
index_1 = 0
proximo_append_termo = ""
proximo_append_catego = ""
proximo_append_descr = ""
for entry_1 in dicionario_list:
    if len(re.findall(r"<b>(.*?)</b>", entry_1)) > 0:
        if index_1 > 0 and index_1 < len(dicionario_list) - 1: # elementos intermédios da lista
            if len(re.findall(r"<b>(.*?)</b>", dicionario_list[index_1 - 1])) > 0 and len(re.findall(r"<b>(.*?)</b>", dicionario_list[index_1 + 1])) > 0:
                proximo_append_termo += re.findall(r"<b>(.*?)</b>", entry_1)[0]
            elif len(re.findall(r"<b>(.*?)</b>", dicionario_list[index_1 - 1])) > 0 and len(re.findall(r"<b>(.*?)</b>", dicionario_list[index_1 + 1])) == 0:
                proximo_append_termo += re.findall(r"<b>(.*?)</b>", entry_1)[0]
                if len(re.findall(r"<i>Categoria:", dicionario_list[index_1 + 1])) > 0:
                    dicionario_termos.append([proximo_append_termo, "com_categoria"])
                else:
                    dicionario_termos.append([proximo_append_termo, "sem_categoria"])
                proximo_append_termo = ""
            elif len(re.findall(r"<b>(.*?)</b>", dicionario_list[index_1 - 1])) == 0 and len(re.findall(r"<b>(.*?)</b>", dicionario_list[index_1 + 1])) == 0:
                proximo_append_termo += re.findall(r"<b>(.*?)</b>", entry_1)[0]
                if len(re.findall(r"<i>Categoria:", dicionario_list[index_1 + 1])) > 0:
                    dicionario_termos.append([proximo_append_termo, "com_categoria"])
                else:
                    dicionario_termos.append([proximo_append_termo, "sem_categoria"])
                proximo_append_termo = ""
            elif len(re.findall(r"<b>(.*?)</b>", dicionario_list[index_1 - 1])) == 0 and len(re.findall(r"<b>(.*?)</b>", dicionario_list[index_1 + 1])) > 0:
                proximo_append_termo += re.findall(r"<b>(.*?)</b>", entry_1)[0]
        elif index_1 == 0: # primeiro elemento da lista
            if len(re.findall(r"<b>(.*?)</b>", dicionario_list[index_1 + 1])) > 0:
                proximo_append_termo += re.findall(r"<b>(.*?)</b>", entry_1)[0]
            elif len(re.findall(r"<b>(.*?)</b>", dicionario_list[index_1 + 1])) == 0:
                proximo_append_termo += re.findall(r"<b>(.*?)</b>", entry_1)[0]
                if len(re.findall(r"<i>Categoria:", dicionario_list[index_1 + 1])) > 0:
                    dicionario_termos.append([proximo_append_termo, "com_categoria"])
                else:
                    dicionario_termos.append([proximo_append_termo, "sem_categoria"])
                proximo_append_termo = ""

    elif len(re.findall(r"<i>Categoria:", entry_1)) == 0:
        if len(re.findall(r"<i>Categoria:", dicionario_list[index_1 - 1])) > 0:
            proximo_append_catego += re.findall(r">(.*?)</text>", entry_1)[0]
            next_width = int(re.findall(r"width=\"(.*?)\"", dicionario_list[index_1 + 1])[0])
            this_width = int(re.findall(r"width=\"(.*?)\"", entry_1)[0])
            if next_width > 223:
                dicionario_catego.append(proximo_append_catego)
                proximo_append_catego = ""
            elif this_width < 218:
                dicionario_catego.append(proximo_append_catego)
                proximo_append_catego = ""
            else:
                token_catego = 1
        elif token_catego == 1:
            next_width = int(re.findall(r"width=\"(.*?)\"", dicionario_list[index_1 + 1])[0])
            proximo_append_catego += re.findall(r">(.*?)</text>", entry_1)[0]
            if next_width > 223:
                dicionario_catego.append(proximo_append_catego)
                proximo_append_catego = ""
                token_catego = 0
        else:
            if index_1 > 0 and index_1 < len(dicionario_list) - 1:  # elementos intermédios da lista
                proximo_append_descr += re.findall(r">(.*?)</text>", entry_1)[0]
                if len(re.findall(r"<b>(.*?)</b>", dicionario_list[index_1 + 1])) > 0:
                    dicionario_descr.append(proximo_append_descr)
                    proximo_append_descr = ""
            elif index_1 == len(dicionario_list) - 1:  # último elemento da lista
                proximo_append_descr += re.findall(r">(.*?)</text>", entry_1)[0]
                dicionario_descr.append(proximo_append_descr)
                proximo_append_descr = ""

    index_1 += 1

dicionario_dict = {}
index_catego = 0
index_descr = 0
for termo in dicionario_termos:
    if termo[1] == "sem_categoria":
        dicionario_dict[termo[0]] = {"categoria": "N/A", "descricao": dicionario_descr[index_descr]}
        index_descr += 1
    else:
        dicionario_dict[termo[0]] = {"categoria": dicionario_catego[index_catego], "descricao": dicionario_descr[index_descr]}
        index_descr += 1
        index_catego += 1

file_out_siglas = open("siglas.xml", "w")
file_out_siglas.write(siglas)
file_out_siglas.close()

file_out_dicionario = open("dicionario.xml", "w")
file_out_dicionario.write(dicionario)
file_out_dicionario.close()

file_out_siglas_dict = open("siglas.json", "w", encoding="utf8")
json.dump(siglas_dict,file_out_siglas_dict, indent=4, ensure_ascii=False)
file_out_siglas_dict.close()

file_out_dicionario_dict = open("dicionario.json", "w", encoding="utf8")
json.dump(dicionario_dict,file_out_dicionario_dict, indent=4, ensure_ascii=False)
file_out_dicionario_dict.close()