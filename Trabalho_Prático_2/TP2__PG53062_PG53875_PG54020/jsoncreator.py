import json

dicionario = open("dicionario.json", "r", encoding ="utf-8")
dicionario_ = json.load(dicionario)
dicionario.close()

siglas = open("siglas.json", "r", encoding ="utf-8")
siglas_ = json.load(siglas)
siglas.close()

dic_keys = list(dicionario_.keys())
sig_keys = list(siglas_.keys())

for termo in dic_keys:
    dicionario_[termo]["siglas"] = {}
    for sig in sig_keys:
        if sig in termo or sig in dicionario_[termo]["descricao"]:
            dicionario_[termo]["siglas"][sig] = siglas_[sig]

dicionario_novo = open("dic_novo.json", "w", encoding="utf-8")
json.dump(dicionario_, dicionario_novo, indent=4, ensure_ascii=False)
dicionario_novo.close()