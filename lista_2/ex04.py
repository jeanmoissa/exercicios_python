#numero de itens na lista
num_lista = int(input("Digite o número de elementos da lista:"))

#criação de uma lista de numeros
lista = [] 

#adição de cada numero na lista
for i in range(num_lista):
    num_item = int(input(f"\nDigite um numero: "))
    lista.append(num_item)

#Organização dos numeros na lista
for i in range(num_lista-1):
    for j in range(num_lista-1-i): 
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print(f"\n-> Lista ordenada: {lista}\n")