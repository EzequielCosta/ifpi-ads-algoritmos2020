cont = [0, 0, 0, 0]
def main():
    global cont
    #PRIMEIRA ETAPA
    print("\n")
    quant_num = int(input("Digite a quantidade de números: "))

    # SEGUNDA ETAPA
    print("\n")
    vetor = [-1] * quant_num

    #TERCEIRA ETAPA
    print("\n")
    for i in range(quant_num):
        numero = int(input("Digite o número desejado: "))
        vetor[i] = numero

    #QUARTA ETAPA
    print("\n")
    verifica_tipo(vetor)
    mostra_tipos_array(cont)

    #QUINTA ETAPA
    print("\n")
    for j in range(len(vetor)):
        if (vetor[j] > 0):
            vetor[j] = vetor[j] * 2
        elif (vetor[j] < 0):
            vetor[j] = vetor[j] / 2

    #SEXTA ETAPA
    print("\n")
    cont = [0,0,0,0]
    verifica_tipo(vetor)
    mostra_tipos_array(cont)

    #SÉTIMA ETAPA
    print("\n")
    print("A média: ",media(vetor))


def verifica_tipo(vetor):
    global cont
    for numero in vetor:
        if (numero % 2 == 0):
            cont[0] = cont[0] + 1
        elif (numero % 2 != 0):
            cont[1] = cont[1] + 1
        if (numero < 0):
            cont[2] = cont[2] + 1
        elif (numero > 0):
            cont[3] = cont[3] + 1



def media (vetor):
    soma = 0
    for a in vetor:
        soma += a
    return soma / (len(vetor))

def mostra_tipos_array(cont):
    print("{0} são pares".format(cont[0]))
    print("{0} são impares".format(cont[1]))
    print("{0} são negativos".format(cont[2]))
    print("{0} são positivos".format(cont[3]))


main()