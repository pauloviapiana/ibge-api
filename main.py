# from fastapi import FastAPI
# app = FastAPI()
import requests

tabela = input('Digite o número da tabela: ')
nivel_geografico = input('Digite o nível geográfico: ')
localidade = input('Digite a localidade: ')

class Get:
    def __init__(self, tabela, nivel_geografico, localidade):
        self.tabela = tabela
        self.nivel_geografico = nivel_geografico
        self.localidade = localidade

    def acessar_tabela(self):
        url = f'https://servicodados.ibge.gov.br/api/v3/agregados/{self.tabela}/periodos/2023/variaveis/603?localidades={self.nivel_geografico}[{self.localidade}]&classificacao=12446[47692]|2009[73535]'
        print(url)
        response = requests.get(url)
        dados_json = response.json()
        for dado in dados_json['resultados'['series'['serie'['2023']]]]:
            print(dado)



consulta = Get(tabela, nivel_geografico, localidade)
consulta.acessar_tabela()

