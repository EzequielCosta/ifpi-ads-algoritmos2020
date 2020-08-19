#Leia N, calcule e escreva 
#os N primeiros termos de seqüência (1, 3,6,10,15,...)

n = int(input("Digite um numero n: "));
contador = 2
inicio = 1

while n > 0:
    print(inicio)
    inicio += contador
    n -= 1
    contador +=1 
    

