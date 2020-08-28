n = int(input("Digite um número n: "))
s = 0
cont = 1
while cont <= n:
    s += 1 / cont
    cont += 1

print("A soma com duas casas decimais é {:.3} ".format(s))
