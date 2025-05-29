""" Calcula o valor total a ser pago por um 
determinado numero de unidades de um produto"""

produto = input("Digite o nome do produto: ")
valor = float(input("Digite o preço unitário R$  "))
quantidade = float(input("Agora digite a quantidade desejada: "))
soma = valor * quantidade
#Explicação da compra
print("\n-----RECIBO DE COMPRA-----\n")

print(f"Você comprou o seguinte produto {produto}.")
print(f"O valor unitário é: {valor}")
print(f"Você comprou {quantidade} unidades de {produto}.")
print(f"O valor total da compra é: R$ {soma :.2f}")