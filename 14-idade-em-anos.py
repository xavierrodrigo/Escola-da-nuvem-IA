from datetime import date

def idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Aproximação, sem considerar anos bissextos
    return idade_dias

# Exemplo de uso
ano = int(input("Digite o ano de nascimento: "))
print(f"Desconsiderando os anos bissextos, você tem {idade_em_dias(ano)} dias de vida.")
