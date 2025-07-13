#operação Basicas   
print("Bem-vindo à calculadora simples!")
print("Escolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite o número da operação (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == '1':
    resultado = num1 + num2
    print("Resultado da soma:", resultado)
elif operacao == '2':
    resultado = num1 - num2
    print("Resultado da subtração:", resultado)
elif operacao == '3':
    resultado = num1 * num2
    print("Resultado da multiplicação:", resultado)
elif operacao == '4':
    if num2 == 0:
        print("Erro! Não é possível dividir por zero.")
    else:
        resultado = num1 / num2
        print("Resultado da divisão:", resultado)
else:
    print("Opção inválida. Tente novamente.")