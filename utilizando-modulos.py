import random
def main():
    """Função principal que executa o programa."""
    print("Bem-vindo ao gerador de senhas!")
    tamanho = int(input("Digite o tamanho da senha (padrão é 8): ") or 8)
    senha = gerar_senha(tamanho)
    print(f"Senha gerada: {senha}")
import string
def gerar_senha(tamanho=8):
    """Gera uma senha aleatória com o tamanho especificado."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
    print("Senha gerada:", gerar_senha(8))