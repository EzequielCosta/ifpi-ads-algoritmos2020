n = int(input("Digite um número n: "))
s = 0
cont = 1
while  n > 0:
    s += cont / (n)
    cont += 1
    n -= 1

print("A soma com duas casas decimais é {:.3} ".format(s))
