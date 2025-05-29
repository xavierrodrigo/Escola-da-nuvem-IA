while True:
    senha = input ("Digite a senha: ")

    if senha.lower() == "sair":
        print ("Programa encerrado. Até logo!")
        break
        
        if len(senha) < 8:
            print("A senha deve ter pelo menos 8 caracteres.")
        continue
    else:
        print ("Ok. Sua senha tem 8 ou mais caracteres.")

        temNumero = False
        
        for caractere in senha:
            if caractere in '0123456789':
                temNumero = True
                print("Número encontrado.")
                break

        if not temNumero:
            print ("A senha deve conter pelo menos um número.")
            continue
        else:
            print ("Ok. Sua senha contém pelo menos um número.")
    print ("Senha forte e válida!")
    break

