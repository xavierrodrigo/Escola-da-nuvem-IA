# Calcular o Indice de Massa Corporal (IMC) de uma pessoa.
peso = float(input("Digite o seu peso em kg: "))
print(f"O seu peso é {peso:.2f} Kilos.")
print("-----------------------------------")
altura = float(input("Digite a sua altura em metros: "))
print(f"Sua altura é {altura:.2f} metros.")
print("-----------------------------------")
#expressão do cálculo
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}.")
print("De acordo com o resultado, sua classificação é: ")
# classificação do IMC
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade grau I")
elif imc < 40:
    print("Obesidade grau II (severa)")
else:
    print("Obesidade grau III (mórbida)")