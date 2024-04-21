from flask import Flask, render_template, redirect, url_for, request
import json
import re
import os

app = Flask(__name__)

file = open('conceitos_v2.json')
conceitos = json.load(file)


@app.route('/')
def home():  # put application's code here
    return render_template('home.html', title='HOME')


@app.route('/conceitos')
def conceitos_page():
    return render_template('conceitos.html', title = 'CONCEITOS', conceitos = conceitos)


@app.route('/conceitos/<string:Conceito>')
def conceito(Conceito):
    Conceito = re.sub(r"%", r"/", Conceito)
    Conceito = re.sub(r"\$", r" ", Conceito)
    if Conceito in conceitos.keys():
        if Conceito != 'Significado':
            descricao = conceitos[Conceito]['desc']
            ingles = conceitos[Conceito]['en']
            entrada = (Conceito, descricao, ingles)
            return render_template('conceito.html', title=Conceito, entrada=entrada)
        else:
            return redirect('http://127.0.0.1:5000/conceitos')
    else:
        return render_template('err_page.html', title="ERRO")


@app.route("/conceitos", methods=["POST"])
def adicionar_conceitos():
    designacao = request.form.get("designacao")
    descricao = request.form.get("descricao")
    en = request.form.get("en")
    termo = request.form.get("termo")

    print(designacao, descricao, en, termo)

    if termo != None:
        conceitos_match = {}
        keys = conceitos.keys()
        for key in keys:
            if key == "Significado":
                conceitos_match[key] = conceitos[key]
            elif (" "+termo+" ") in key.lower() or (" "+termo) in key.lower() or (termo+" ") in key.lower():
                conceitos_match[key] = conceitos[key]
            elif (" "+termo+" ") in conceitos[key]["desc"].lower() or (" "+termo+".") in conceitos[key]["desc"].lower() or (termo+" ") in conceitos[key]["desc"].lower():
                conceitos_match[key] = conceitos[key]

        return render_template("conceitos.html", title='CONCEITOS', conceitos=conceitos_match)

    else:
        conceitos[designacao] = {
            "desc": descricao,
            "en": en
        }

        return render_template("conceitos.html", title='CONCEITOS', conceitos=conceitos)


@app.route("/conceitos/<string:Conceito>", methods=["DELETE"])
def delete_conceitos(Conceito):
    os.rename("conceitos_v2.json", "conceitos_v2_backup.json")
    file_out = open("conceitos_v2.json","w")
    del conceitos[Conceito]
    json.dump(conceitos, file_out, indent=4, ensure_ascii=False)
    file_out.close()
    return render_template("conceitos.html", conceitos=conceitos)

@app.route("/tabela")
def tabela():
    conceitos_tabela = conceitos.copy()
    conceitos_tabela.pop("Significado")
    return render_template("tabela.html", title="TABELA", conceitos=conceitos_tabela)


if __name__ == '__main__':
    app.run(host="localhost", port=4002, debug=True)
