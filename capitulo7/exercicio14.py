#Leia  N,  calcule  e escrevao  maior  quadrado  menor  ou 
#  igual  a  N.  Por  exemplo,  se  N  for  igual  a  38, 
#  o maior quadrado menor que 38 é 36 (quadrado de 6).


n = int(input("Digite um numero n: "));
contador = 0;
while (contador ** 2) <= n:
    contador += 1

print((contador-1) ** 2)