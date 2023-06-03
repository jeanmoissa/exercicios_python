numero = int(input("Digite um numero real:"))
numero +=1
fatorial = 1

for i in range (1,numero):
    fatorial *=i

print(f"O fatorial do numero {numero-1} é {fatorial}")