import math
oposto = float (input("Digite o valor do cateto oposto: "))
adjacente = float (input("digite o valor do cateto adjacente: "))
hipo = math.hypot(oposto, adjacente)

#hipo = (oposto**2 + adjacente**2) ** (1/2) 
#1 modelo utilizando import, e o modelo 2 sem utilização 

print("O valor da hipotenusa é: {} " .format(hipo))
