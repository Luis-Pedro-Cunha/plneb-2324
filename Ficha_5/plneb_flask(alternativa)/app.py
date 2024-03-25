from flask import Flask, render_template, redirect, url_for
import json
import re

app = Flask(__name__)

file = open('conceitos.json')
conceitos = json.load(file)

@app.route('/')
def home():  # put application's code here
    return render_template('home.html', title = 'HOME')

@app.route('/conceitos')
def conceitos_page():
    return render_template('conceitos.html', title = 'CONCEITOS', conceitos = conceitos)

@app.route('/conceitos/<string:Conceito>')
def conceito(Conceito):
    Conceito = re.sub(r"%", r"/", Conceito)
    Conceito = re.sub(r"\$", r" ", Conceito)

    if Conceito != 'Significado':
        descricao = conceitos[Conceito]
        entrada = (Conceito, descricao)
        return render_template('conceito.html', title=Conceito, entrada=entrada)
    else:
        return redirect('http://127.0.0.1:5000/conceitos')

if __name__ == '__main__':
    app.run(host="localhost", port=4002, debug=True)
