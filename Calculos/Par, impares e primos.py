num = int (input("Digite um numero: "))
resultado = num % 2
if resultado == 0 and num != 2:
    print("{} é um numero par e não é primo".format(num))
elif num == 2 :
    print("{} é um numero par e é primo ".format(num))
else:
    print("{} é um numero impar e é primo".format(num))
