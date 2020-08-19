"""
Leia  as  variáveis  A0,  Limite  e 
 R  e escrevaos  valores  menores  que  
 Limite  gerados  pela  Progressão Aritmética que tem 
 por valor inicial A0e razão R.
"""

A0 = int(input("Digite o valor inicial da PG: "))
limite = int(input("Digite o limite : "))
R = int(input("Digite a razão desta PG : "))
contador = 1
valor = 0

while (valor * R) < limite :
    valor = A0 * R**(contador-1)
    print(valor)
    contador += 1