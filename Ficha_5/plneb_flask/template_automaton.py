import json
import re

file = open('conceitos.json')
conceitos = json.load(file)

for conceito in conceitos:
    descricao = conceitos[conceito]
    html = """
            {% extends 'parent.html' %}
        
            {% block head %}
            <title>{{ title }}</title>
            {% endblock %}
            
            {% block body %}
            <p class='fs-1' style='text-align: center; text-decoration-line: underline; text-transform: capitalize; text-shadow: 2px 2px grey;'>
            """ + conceito + """
            </p>
            <p class='fs-5' style='text-align: justify; padding-left: 20%; padding-right: 20%'>
            """ + descricao + """
            </p>
            {% endblock %}
            """

    conceito = re.sub(r"/", r"-", conceito)

    file_out = open(f"templates/{conceito}.html", "w")
    file_out.write(html)
    file_out.close()
