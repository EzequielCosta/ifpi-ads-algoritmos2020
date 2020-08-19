#Leia N e uma lista de N números e escrevaa soma
# e a média de todos os números da lista.


n = int(input("Digite um numero n: "));
contador = n
soma = 0

while contador > 0:
    soma += int(input("Digite o {0} número: ".format((n-contador)+1)))
    contador -= 1

print("A soma dos números dados é: {0}".format(soma))
print("A média, com duas casas decimais, dos números dados é: {:.2f}".format(soma/n))
