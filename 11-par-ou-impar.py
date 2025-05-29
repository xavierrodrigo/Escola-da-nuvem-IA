def main():
    numeroPar = 0
    numeroImpar = 0

    while True:
        entrada = (input("Digite um número inteiro ou fim para encerrar: \n"))
        
        if entrada.lower() == 'fim':
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"O número {numero} é par!\n")
                numeroPar +=1
            else:
                print(f"O número {numero} é ímpar!\n")
                numeroImpar +=1

        except ValueError:
            print("ERRO! Digite um número inteiro ou fim para encerrar!")
    print(f"Quantidade de números pares: {numeroPar}\n")
    print(f"Quantidade de números ímpares: {numeroImpar}")

main()

