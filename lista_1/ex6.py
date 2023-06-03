produto = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

if quantidade <= 10:
    valor_final = valor * quantidade
elif 11 <= quantidade <= 20:
    valor_final = valor * quantidade * 0.9  #10% de desconto
elif 21 <= quantidade <= 50:
    valor_final = valor * quantidade * 0.8  #20% de desconto
else:
    valor_final = valor * quantidade * 0.75  #25% de desconto

print(f"Produto comprado:{produto}")
print(f"Valor total a ser pago:R$ {valor_final}")