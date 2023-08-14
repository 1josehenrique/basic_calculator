# FUNÇÕES DO CÓDIGO
def inicio():
  print("Digite: ")
  print(" ")
  print("1 para Soma")
  print("2 para Subtração")
  print("3 para Multiplicação")
  print("4 para Divisão")
  print("5 para Exponenciação")
  print(" ")

def soma():
    
    print("====================")
    print("Você escolheu SOMA!")
    print("====================")
    print("Digite um número: ")
    n1 = float(input())

    print("Digite outro número: ")
    n2 = float(input())

    print("====================")
    resultado = n1 + n2

    print("{} + {} = {}".format(n1, n2, resultado))
    print("====================")

def subtracao():
    print("====================")
    print("Você escolheu SUBTRAÇÃO!")
    print("====================")
    print("Digite um número: ")
    n1 = float(input())

    print("Digite outro número: ")
    n2 = float(input())

    print("====================")
    resultado = n1 - n2

    print("{} - {} = {}".format(n1, n2, resultado))
    print("====================")

def multiplicacao():
    print("====================")
    print("Você escolheu MULTIPLICAÇÃO!")
    print("====================")
    print("Digite um número: ")
    n1 = float(input())

    print("Digite outro número: ")
    n2 = float(input())

    print("====================")
    resultado = n1 * n2

    print("{} x {} = {}".format(n1, n2, resultado))
    print("====================")

def divisao():
    print("====================")
    print("Você escolheu DIVISÃO!")
    print("====================")
    print("Digite um número: ")
    n1 = float(input())

    print("Digite outro número: ")
    n2 = float(input())

    print("====================")
    resultado = n1 / n2

    print("{} / {} = {}".format(n1, n2, resultado))
    print("====================")

def exponenciacao():
    print("====================")
    print("Você escolheu EXPONENCIAÇÃO!")
    print("====================")
    print("Valor da base: ")
    base = float(input())

    print("Valor do expoente: ")
    expoente = float(input())

    print("====================")
    resultado = pow(base, expoente)

    print("{} ^ {} = {}".format(base, expoente, resultado))
    print("====================")

# ESTRUTURA DE REPETIÇÃO FAZENDO USO DAS FUNÇÕES 
while True:
  inicio()
  modo = int(input())

  if modo == 1:
    soma()

  elif modo == 2:  
    subtracao()

  elif modo == 3:  
     multiplicacao()

  elif modo == 4:  
    divisao()

  elif modo == 5:  
    exponenciacao()
    
  resposta = input("Deseja fazer outro cálculo? (s/n): ")
  if resposta.lower() != 's':
    break