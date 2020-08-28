# A  prefeitura  de  uma  cidade  fez  uma  pesquisa  entre  seus  habitantes,
# coletando  dados  sobre  o  salário  e número  de  filhos. Escreva  um algoritmo que
# leia  o  salário  e  o  número  de  filhos  de    N  habitantes  e escreva:
# a)média de salário da população;
# b)média de número de filhos;
# c)percentual de pessoas com salário de até R$ 1.000,00.

media_salario = 0
media_filhos = 0
pessoas_menos_de_mil = 0
n = int(input("Digite o número de habitantes: "))
print("")
quantidade_habitantes = n

while n > 0:
    salario = float(input("Digite o valor salarial do funcionário: "))
    media_salario += salario
    media_filhos += int(input("Digite a quantidade de filhos: "))
    if (salario <= 1000.00):
        pessoas_menos_de_mil += 1
    n -= 1
    print("")

print("A média do salário da população é: {:.2f}".format(media_salario / quantidade_habitantes))
print("A média do número de filhos da população é {:.2f}".format(media_filhos/quantidade_habitantes))
print("O percentual de pessoas com o salário abaixo ou igual à R$ 1000.00: {:.2f} %".format((pessoas_menos_de_mil * 100)/quantidade_habitantes))