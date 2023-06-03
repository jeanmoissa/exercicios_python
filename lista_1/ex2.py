#Entrada de dados
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

#calcula IMC
IMC = peso / ((altura/100) ** 2)

#Avaliação de IMC
if IMC <= 18.5:
    print("Abaixo do peso normal.")
elif 18.5 < IMC <= 25:
    print("Peso Normal.")
elif 25 < IMC <= 30:
    print("Acima do peso normal.")
else:
    print("Obesidade.")

