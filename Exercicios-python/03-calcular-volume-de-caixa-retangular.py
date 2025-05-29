#Calcular volume de caixa retangular
# volume = largura * altura * profundidade
largura = input("Digite a largura da caixa: ")
altura = input("Digite a altura da caixa: ")
profundidade = input("Digite a profundidade da caixa: ")
# Conversão para numeros decimais
volume = float(largura) * float(altura) * float(profundidade)
# resultado
print("O volume da caixa retangular é:", volume , "m³")