import requests

cep = input("Digite o CEP (somente números): ")

url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()  
    # Verifica se o CEP existe
    if "erro" not in dados:
        logradouro = dados.get("logradouro")
        bairro = dados.get("bairro")
        cidade = dados.get("localidade")
        estado = dados.get("uf")

        # informações do endereço
        print(f"Logradouro: {logradouro}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")
    else:
        print("CEP não encontrado.")
else:
    print("Erro ao consultar o CEP. Tente novamente.")
