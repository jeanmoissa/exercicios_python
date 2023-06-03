import random

num_random = random.randint(1,1000)

for num_sorteio in range (0,1000):
    num_palpite=int(input("Digite seu palpite entre 0 e 1000: "))

    if(num_palpite == num_random):
        print(f"Você acertou o numero sorteado: {num_random} !!!")
        break
    elif(num_palpite < num_random):
        print("-> Palpite MENOR que o numero sorteado.\n")
    elif(num_palpite > num_random):
        print("-> Palpite MAIOR que o numero sorteado.\n")