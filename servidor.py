import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def vendasTotais():
    tabela = pd.read_csv('dados.csv')
    somaVendas = tabela['Vendas'].sum()
    resposta = {'Total das vendas': somaVendas}
    return jsonify(resposta)

app.run()
