preço = float(input("digite o valor do produto"))
desconto = float(input("digite o valor do desconto em %"))
calculo = preço - (preço * desconto)/100
desconto = (preço * desconto)/100
print("o valor do produto vai custar {} e seu desconto foi de {}" .format(calculo, desconto))
