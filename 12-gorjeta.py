def calcularGorjeta(valorConta, porcentagemGorjeta):
    gorjeta = valorConta * (porcentagemGorjeta / 100)
    return gorjeta

print(f"O valor da gorjeta é: {calcularGorjeta(130, 12)}")