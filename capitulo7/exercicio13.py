#Leia N e uma lista de N números 
# e escreva o maior número da lista

n = int(input("Digite um numero n: "));
contador = n
primeiro = 0
while contador > 0:
    segundo = int(input("Digite o {0} número: ".format((n-contador)+1)))
    if (segundo > primeiro):
        primeiro = segundo
    
    contador -= 1

print(primeiro)
