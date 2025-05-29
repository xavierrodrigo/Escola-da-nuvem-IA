# Classifica a faixa etária de uma pessoa com base na idade
idade = int(input("Digite a sua idade: "))

if idade < 0:
    print("Idade inválida! Digite uma idade igual ou maior que 0!")
elif idade < 13:
    print("Você é uma criança!")
elif idade >= 13 and idade <= 17:
    print("Você é um adolescente!")
elif idade >= 18 and idade <= 59:
    print("Você é um adulto!")
else:
    print("Você é um idoso!")