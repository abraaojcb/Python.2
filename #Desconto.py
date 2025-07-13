#Desconto
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o desconto (%): "))
valor_descontado = preco * (desconto / 100)
preco_final = preco - valor_descontado
print(f"O valor com desconto é: R${preco_final:.2f}")