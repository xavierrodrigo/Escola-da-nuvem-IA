import random
import string

def gerarSenha(tamanhoSenha):
    caracteres = string.digits + string.ascii_letters + string.punctuation

    senha = ''
    for s in range(tamanhoSenha):
        senha += (random.choice(caracteres))
    return senha

numCaracteres = int(input("\nDigite a quantidade de caracters da senhas: "))

senha = gerarSenha(numCaracteres)
print(f"Esta é sua senha: {senha}\n")

