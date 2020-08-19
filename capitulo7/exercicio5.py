numero = int(input("Digite um número: "))
contador = 1
resultado = 1

while contador <= numero:
    resultado *= contador
    contador += 1
    
print("O fatorial de {0} é: {1}".format(numero,resultado))