"""
Leia  as  variáveis  A0,  Limite  e 
 R  e escrevaos  valores  menores  que  
 Limite  gerados  pela  Progressão Aritmética que tem 
 por valor inicial A0e razão R.
"""

A0 = int(input("Digite o valor inicial da PA: "))
limite = int(input("Digite o limite : "))
R = int(input("Digite a razão desta PA : "))
contador = 1
valor = 0

while (valor+R) < limite :
    valor = A0 + (contador - 1 ) * R
    print(valor)
    contador += 1