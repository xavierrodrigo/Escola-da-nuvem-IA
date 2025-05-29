while True:    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        operacao = input("Digite a operação (+, -, *, /): ")
        
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("ERRO: Divisão por zero não é permitida!\n Digite um número maior que zero")
                continue
            resultado = num1 / num2
        else:
            print("Operação inválida! Utilize apenas: +, -, *, /")
            continue

        print(f"Resultado: {resultado}")
        break
    except ValueError:
        print("ERRO: Entrada inválida! Por favor, insira números válidos.")