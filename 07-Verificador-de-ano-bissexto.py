# Saber se o ano digitado é bissexto.
# - Um ano e bissexto se for divisivel por 4;
""" - Mas anos divisiveis por 100 so sao bissextos
se tambem forem divisiveis por 400."""

ano  = int(input("Digite o ano a ser verificado: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    # Se o ano for divisível por 4 e não for divisível por 100
    # ou se for divisível por 400, então é bissexto
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")