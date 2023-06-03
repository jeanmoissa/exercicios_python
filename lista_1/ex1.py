vel_carro = int(input("Digite a velocidade do veiculo: "))
vel_max = int(input("Digite a velocidade máxima da via: "))


if vel_carro <= (vel_max+10):
    print("valor da multa: R$ 100,00")

#elif ((vel_max+11) <= vel_carro) or (vel_carro <= (vel_max+30)):
elif (vel_max+11) <= vel_carro <= (vel_max+30):
    print("valor da multa: R$ 183,00")

else:
    print("valor da multa: R$ 347,00")