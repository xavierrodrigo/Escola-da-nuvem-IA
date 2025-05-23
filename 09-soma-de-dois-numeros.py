
#calcumo entre dois numeros
num1 = input ("Digite o primeiro número: ")
num2 = input ("Digite o segundo número: ")
soma = int(num1) + int(num2)
# A partir daqui são implementadas outras operações
subtracao = int(num1) - int(num2)
multiplicacao = int(num1) * int(num2)
divisao = int(num1) / int(num2)
divisaoInteira = int(num1) // int(num2)
potencia = int(num1) ** int(num2)
resto = int(num1) % int(num2)
print (f"A soma de {num1} e {num2} é: {soma}")
       
# A partir daqui são resultados das implementações.
print (f"A subtracao de {num1} e {num2} é: {subtracao}")
print (f"A multiplicacao de {num1} e {num2} é: {multiplicacao}")
print (f"A divisao de {num1} e {num2} é: {divisao}")
print (f"A divisão exata de {num1} e {num2} é: {divisaoInteira}")
print (f"A potência de {num1} e {num2} é: {potencia}")
print (f"O resto de {num1} e {num2} é: {resto}")