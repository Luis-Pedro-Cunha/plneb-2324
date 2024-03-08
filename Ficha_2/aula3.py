import re 

filename = "../Dados/dicionario_medico.txt"
file = open(filename)
texto = file.read()

#data cleaning
texto = re.sub(r"\f","",texto)

#marcar designações

texto = re.sub(r'\n\n(.+)',r'\n\n@\1',texto)
texto = re.sub(r'@(.+)\n\n@',r'@\1\n',texto)

#Extrair termos 
#designacoes = []
#designacoes = re.findall(r'@(.+)\n',texto)

termos = []
termos = re.findall(r'@(.+)\n([^@]+)',texto)


# Gerar HTML
head = """
<!DOCTYPE html>
<html lang="pt" class="pagina">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="aula3.css">
    <link rel="icon" type="image/x-icon" href="illustration-of-book-icon-free-vector.ico" sizes="16x16 32x32">
    <title>Dicionário Médico</title>
</head>"""
titulo = "<div class=\"cab1\"><h3> Dicionário Médico </h3></div>"
descricao = "<div class=\"cab2\"><p> Este é um dicionário médico desenvolvido na disciplina de SPLNEB </p></div>"

body = "<body><div class='conteudo'>"
script1 = """
<script>
    function scrollToSection() {
        var inputContent = document.getElementById("pesquisa").value;
        var section = document.getElementById(inputContent);
        if (section) {
            window.scrollTo({
                top: section.offsetTop,
                behavior: 'smooth'
            });
        } else {
            alert("Section not found!");
        }
    }
</script>
"""

body += script1
for termo in termos:
    body += f"<div id=\"{termo[0]}\">"
    body += f"<h5> {termo[0]} </h5>"
    body += f"<p> {termo[1]} </p>"
    if termos.index(termo) < len(termos)-1:
        body += "<hr/>"

body += "</div></body>"



html = head + "<div class=\"cabecalho\">" + titulo + descricao + """<div class="cab3">
            <input class="barra" type="text" id="pesquisa" placeholder="Palavra a encontrar" name="pesquisa" required>
            <button class="botao" onclick="scrollToSection()">Pesquisa</button>
        </div></div>""" + "<div class=\"dicionario\">" + body + "</div>"
#print(html)

file_out = open("aula3.html", "w")
file_out.write(html)
file_out.close()