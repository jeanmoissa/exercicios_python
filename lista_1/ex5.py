ano = int(input("Digite o ano: "))

if (ano % 400 == 0):
    print(f"o ano de {ano} é ano bissexto.")
elif (ano % 4 == 0 and ano % 100 != 0):
    print(f"o ano de {ano} é ano bissexto.")
else:
    print(f"O ano de {ano} não é ano bissexto.")