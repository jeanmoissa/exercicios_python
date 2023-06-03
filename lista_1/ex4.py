from datetime import date

dia_nasc = int(input("Digite o dia do seu nascimento: "))
mes_nasc = int(input("Digite o mês do seu nascimento: "))
ano_nasc = int(input("Digite o ano do seu nascimento: "))

#seleciona dia de hoje
data_atual = date.today()

#calcula idade de acordo com o ano
idade = data_atual.year - ano_nasc

#verifica se o mes do aniversario ja passou
if mes_nasc > data_atual.month or (mes_nasc == data_atual.month and dia_nasc > data_atual.day):
    idade -= 1

#imprime idade
print(f"Você possui:{idade} anos.")