# Solicitar entrada do usuário
valor1 = float(input("Digite o primeiro valor real: "))
valor2 = float(input("Digite o segundo valor real: "))

# Exibir menu de opções
print("Selecione a operação desejada:")
print("+ Soma")
print("- Subtração")
print("/ Divisão")
print("* Multiplicação")
print("% Resto da Divisão")

operacao = input("Digite a operação desejada: ")

match operacao:
    case '+':
        resultado = valor1 + valor2
    case '-':
        resultado = valor1 - valor2
    case '/':
        resultado = valor1 / valor2
    case '*':
        resultado = valor1 * valor2
    case '%':
        resultado = valor1 % valor2

# Exibir o resultado
print(f"Resultado da operação:{resultado}")