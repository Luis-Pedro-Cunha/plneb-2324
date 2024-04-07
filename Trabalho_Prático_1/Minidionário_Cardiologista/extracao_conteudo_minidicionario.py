import re
import json

file = open("08. Minidicionário de Cardiologista Autor Ricardo Silveira Mello.xml",encoding="utf-8")
texto = file.read()

#LIMPEZA DO CONTEÚDO
texto = re.sub(r'(<text.+font="6".+</text>)',r'',texto) #remover os termos no inicio das páginas que dizem o primeiro e último termo da página
texto = re.sub(r'(<text.+font="5".+</text>)',r'',texto) #remover números das páginas
texto = re.sub(r'(<text.+font="9".+</text>)',r'',texto) #remover números das páginas
texto = re.sub(r'(<text.+font="15".+</text>)',r'',texto) #remover números das páginas
texto = re.sub(r'(<text.+font="12".+</text>)',r'',texto)
texto = re.sub(r'<image.+?>',r'',texto) #remover as imagens
texto = re.sub(r'<page.+>?', r'', texto) #eliminar as informações sobre as páginas
texto = re.sub(r'</page>', r'', texto)
texto = re.sub(r'\n\s*\n', r'\n', texto) #remover linhas em branco
texto = re.sub(r'­',r'', texto)

partes = re.split(r'@',texto)

with open('novo_xml.xml', 'w',encoding="utf-8") as file:
    file.write(texto)


#LIMPEZA DE CADA UMA DAS SECÇÕES
partes[0] = re.sub(r'<text.+?>',r'', partes[0])
partes[0] = re.sub(r'</text>',r'',partes[0])
partes[0] = re.sub(r'\n\s*\n', r'\n', partes[0])
partes[0] = re.sub(r'^\s',r'',partes[0]) #retirar espaços no inicio da linha
partes[0] = re.sub(r'</b>\n<b>',r'',partes[0]) #juntar as cenas a bold
partes[0] = re.sub(r'\n',r'',partes[0])
partes[0] = re.sub(r'<b>',r'\n\n@',partes[0])
partes[0] = re.sub(r'\s–\s*<\/b>',r'@\n',partes[0])

partes[1] = re.sub(r'<text.+?>',r'', partes[1])
partes[1] = re.sub(r'</text>',r'',partes[1])
partes[1] = re.sub(r'\n\s*\n', r'\n', partes[1])
partes[1] = re.sub(r'^\s',r'',partes[1]) #retirar espaços no inicio da linha
partes[1] = re.sub(r'</b>\n<b>',r'',partes[1]) #juntar as cenas a bold
partes[1] = re.sub(r'\n',r'',partes[1])
partes[1] = re.sub(r'<b>',r'\n\n@',partes[1])
partes[1] = re.sub(r'\s–\s*<\/b>',r'@\n',partes[1])

with open('EN-PT.xml','w',encoding="utf-8") as file1:
    file1.write(partes[0])

with open('PT-EN.xml', 'w',encoding="utf-8") as file2:
    file2.write(partes[1])


#EXTRAÇÃO DOS TERMOS
EN_PT = open("EN-PT.xml",encoding="utf-8")
en_pt = EN_PT.read()
conceitos_enpt = re.findall(r'@(.+)@\n(.*)', en_pt)
dic_enpt = dict(conceitos_enpt)

PT_EN = open("PT-EN.xml",encoding="utf-8")
pt_en = PT_EN.read()
conceitos_pten = re.findall(r'@(.+)@\n(.*)', pt_en)
dic_pten = dict(conceitos_pten)


#CRIAÇÃO DOS FICHEIROS JSON
file_en_pt = open("EN_PT.json","w", encoding = "utf-8")
json.dump(dic_enpt, file_en_pt, indent=4, ensure_ascii=False)
file_en_pt.close()

file_pt_en = open("PT_EN.json","w", encoding = "utf-8")
json.dump(dic_pten, file_pt_en, indent=4, ensure_ascii=False)
file_pt_en.close()