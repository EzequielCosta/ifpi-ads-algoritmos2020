#Leia   um   número   N,   calcule   e escreva os   N   primeiros
#    termos   de   seqüência   de   Fibonacci (0,1,1,2,3,5,8,...).O valor
#  lido para N sempre será maior ou igual a 2

n = int(input("Digite um numero n: "));
auxiliar = 0
inicio = 1
soma = 0

while n > 0:
    print(soma)
    auxiliar = soma
    soma += inicio    
    inicio = auxiliar
    n -= 1
