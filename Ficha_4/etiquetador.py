import json
import re

file_conceitos = open("conceitos_v2.json", encoding='utf-8')
file_livro = open("LIVRO-Doenças-do-Aparelho-Digestivo.txt", encoding='utf-8')

header = """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="aula3.css">
    <link rel="icon" type="image/x-icon" href="illustration-of-book-icon-free-vector.ico" sizes="16x16 32x32">
    <title>Dicionário Médico</title>
</head>"""
texto = file_livro.read()
conceitos = json.load(file_conceitos)

blacklist = ["e", "de", "para", "pelo", "os", "são", "este"]

conceitos_min = { chave.lower(): [conceitos[chave]['desc'], conceitos[chave]['en']] for chave in conceitos}

texto = re.sub(r'\n',r'<br>', texto)
texto = re.sub(r'\f', r'<hr>', texto)
def etiquetador(matched):
    palavra = matched[0]
    original = palavra
    palavra = palavra.lower()
    if palavra in conceitos_min and palavra not in blacklist:
        descricao = conceitos_min[palavra][0]
        ingles = conceitos_min[palavra][1]
        etiqueta = f"<a href='' title='Descrição: {descricao}\n\nTradução para inglês: {ingles}'>{original}</a>"
        return etiqueta
    else:
        return original


expressao = r'[\wáéçãóõéíêâú]+'
texto = re.sub(expressao,etiquetador ,texto, flags=re.IGNORECASE)
texto_final = header + texto
file_out = open("livro.html", "w")
print(texto_final, file=file_out)


