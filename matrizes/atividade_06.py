def main():

    n = list(input("Digite a quantidade de elementos do vetor: "))
    print("Número em decimal: ",converte_para_decimal(n))
    print("Número em hexadecimal: ", converte_para_hexadecimal(n))

def converte_para_decimal(num_binario):
    num_binario = num_binario[::-1]
    resultado = 0
    for i in range(len(num_binario)):
        correspondente = 2 ** i
        correspondente *= int(num_binario[i])
        resultado += correspondente
    return resultado

def converte_para_hexadecimal(num_binario):

    num_binario = list(num_binario)
    resultado = 0
    resultado_completo = ''
    while ((len(num_binario)) % 4 != 0):
        num_binario = ['0'] + num_binario
        #print(len(num_binario)+1)
    num_binario = list(num_binario[::-1])
    while (len(num_binario) % 4 == 0 and len(num_binario) != 0 ):

        for i in range(4):
            correspondente = 2 ** i
            correspondente *= int(num_binario[i])
            resultado += correspondente
            if (resultado == 10):
                resultado = 'A'
            elif(resultado == 11):
                resultado = 'B'
            elif (resultado == 12):
                resultado = 'C'
            elif (resultado == 13):
                resultado = 'D'
            elif (resultado == 14):
                resultado = 'E'
            elif (resultado == 15):
                resultado = 'F'

        resultado_completo += str(resultado)

        num_binario.pop(0)
        num_binario.pop(0)
        num_binario.pop(0)
        num_binario.pop(0)
        resultado = 0
    return (resultado_completo[::-1])


main()