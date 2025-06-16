"""Crie um programa que gera um perfil de usuário aleatório
usando a API "Random User Generator". 
O programa deve exibir o nome, email e país do usuário gerado."""

import requests
resposta = requests.get("https://randomuser.me/api/")

# verifica a respostaa da requisição
if resposta.status_code == 200:
    dados = resposta.json()

    # extrai os dados
    usuario = dados['results'][0]
    nomeCompleto = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']

    print("Perfil de Usuário Aleatório\n")
    print(f"Nome: {nomeCompleto}")
    print(f"Email: {email}")
    print(f"País: {pais}")
else:
    print("Erro ao acessar a API")