from datetime import datetime
import random

def info_usuario():
    nome = input('Olá, digite o seu nome:\n')
    print("====================")
    idade = int(input('Quantos anos você tem?\n'))
    print("====================")
    dia = (datetime.now().day)
    mes = (datetime.now().month)
    ano = (datetime.now().year)
    cartoes = ['R$50,00','R$250,00','R$125,00']
    cartao = (random.choice(cartoes))
    aniversario = datetime.strptime(input('Qual a data do seu aniversário?\n'),'%d/%m/%Y')
    print("====================")
    print(f'Olá {nome}, seu registro foi concluido com sucesso no dia {dia}/{mes}/{ano}.\nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao}.')
   
info_usuario()