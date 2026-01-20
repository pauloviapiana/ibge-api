# import requests
# from fastapi import FastAPI

# app = FastAPI()

# @app.get('/api/10026/2023/sc')
# def get_10026_sc():
#     url = 'https://servicodados.ibge.gov.br/api/v3/agregados/10026/periodos/-6/variaveis/603?localidades=N3[42]&classificacao=12446[47692]|2009[73535]'
#     response = requests.get(url)
#     if (response.status_code == 200):
#         dados_json = response.json()
#         return dados_json
#     else:
#         print(response.status_code)


# #@app.get('/api/{tabela}/2023/{localidade}')
# def consulta_tabela():
#     url = https://servicodados.ibge.gov.br/api/v3/agregados/{tabela}/periodos/-6/variaveis/603?localidades{localidade}&classificacao=12446[47692]|2009[73535]

# tabela = o que o usuario selecionar na tela
# regiao = o que o usuario selecionar na tela      

