import json
import re

ficheiro = open("PT_EN.json", "r", encoding="UTF-8")
dicionarioPTEN = json.load(ficheiro)
ficheiro.close()
chavePTEN = list(dicionarioPTEN.keys())

ficheiro = open("EN_PT.json", "r", encoding="UTF-8")
dicionarioENPT = json.load(ficheiro)
ficheiro.close()
chaveENPT = list(dicionarioENPT.keys())

#Tratamento
def tratamento(chaves, dicionario, nome_ficheiro):
    novodicti = {}
    for key in chaves:
        if len(re.findall(r"/", key)) > 0: #encontrar keys que contêm múltiplos termos
            newkeys = key.split("/") #separar as keys nos termos que as compõem
            for i, newkey in enumerate(newkeys):
                newkey = newkey.strip(" ")
                if len(re.findall(r"/", dicionario[key])) > 0: #encontar valores que contêm múltiplos termos
                    newvalues = dicionario[key].split("/") #separar os valores nos termos que os compõem
                    for j, newvalue in enumerate(newvalues):
                        newvalue = newvalue.strip(" ")
                        if i == j: #encontra o match newkey-newvalue
                            novodicti[newkey.lower()] = newvalue.lower() #para cada termo é adiconado uma nova entrada ao novo dicionário com a sua respetiva tradução
                else:
                    novodicti[newkey.lower()] = dicionario[key].lower() #para cada termo vai colocar o valor igual
        elif len(re.findall(r"/", key)) == 0 and len(re.findall(r"/", dicionario[key])) > 0:
            newvalues = dicionario[key].split("/")
            newnewvalues = []
            for newvalue in newvalues:
                newvalue = newvalue.strip(" ")
                newnewvalues.append(newvalue.lower())
            novodicti[key.lower()] = newnewvalues
        else:
           novodicti[key.lower()] = dicionario[key].lower()

    ficheiro = open(nome_ficheiro, "w", encoding="UTF-8")
    json.dump(novodicti, ficheiro, indent=4, ensure_ascii=False)
    ficheiro.close()
    print(f"Criação do ficheiro {nome_ficheiro} concluída!")

    return

tratamento(chavePTEN, dicionarioPTEN, "novo_PT_EN.json")
tratamento(chaveENPT, dicionarioENPT, "novo_EN_PT.json")
