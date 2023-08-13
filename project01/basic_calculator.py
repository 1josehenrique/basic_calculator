print("Olá, Essa é uma Calculadora que irá te auxiliar em seus cálculos!")

while True:
    operation = int(input("Escolha qual tipo de operação deseja fazer:\n(1) ADIÇÃO\n(2) SUBTRAÇÃO\n(3) MULTIPLICAÇÃO\n(4) DIVISÃO\n"))

    if operation == 1:
        print("--------------------------------")
        print("Você escolheu ADIÇÃO!\nDigite um número:")
        num1 = int(input())
        print("---------------------------------")
        print("Digite outro número:")
        num2 = int(input())
        calc = num1 + num2
        print("---------------------------------")
        print(f"RESULTADO: {calc}")
        print("---------------------------------")

    if operation == 2 :
        print("---------------------------------")
        print("Você escolheu SUBTRAÇÃO!\nDigite um número:")
        num1 = int(input())
        print("---------------------------------")
        print("Digite outro número:")
        num2 = int(input())
        calc = num1 - num2
        print("---------------------------------")
        print(f"RESULTADO: {calc}")
        print("---------------------------------")

    if operation == 3 :
        print("---------------------------------")
        print("Você escolheu MULTIPLICAÇÃO!\nDigite um número:")
        num1 = int(input())
        print("---------------------------------")
        print("Digite outro número:")
        num2 = int(input())
        calc = num1 * num2
        print("---------------------------------")
        print(f"RESULTADO: {calc}")
        print("---------------------------------")

    if operation == 4 :
        print("---------------------------------")
        print("Você escolheu DIVISÃO!\nDigite um número:")
        num1 = int(input())
        print("---------------------------------")
        print("Digite outro número:")
        num2 = int(input())
        calc = num1 / num2
        print("---------------------------------")
        print(f"RESULTADO: {calc}")
        print("---------------------------------")

    if operation >= 5:
        print("Modo de operação inválida!\nDigite um modo de operação válido!")
        print("---------------------------------")

    if operation == 0:
        print("Modo de operação inválida!\nDigite um modo de operação válido!".upper())
        print("---------------------------------")

    resposta = input("Deseja fazer outro cálculo? (s/n): ")
    if resposta.lower() != "s":
        break