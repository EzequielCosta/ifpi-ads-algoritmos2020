# Leia  um  vetor  com  N  elementos,  encontre  e  escreva  o  maior
# e  o  menor elemento  e  suasrespectivas posiçõesno vetor


def main():
    n = int(input("Digite a quantidade de elementos: "))
    vetor = []
    for i in range(n):
        vetor.append(int(input("Digite o elemento: ")))

    maior_elemento = localiza_maior(vetor)
    menor_elemento = localiza_menor(vetor)

    print("O maior elemento de indice {0} é {1}: ".format(maior_elemento[1],maior_elemento[0]))
    print("O menor elemento de indice {0} é {1}: ".format(menor_elemento[1],menor_elemento[0]))




def localiza_maior(vetor):
    elemento_maior = [vetor[0],0]
    for i in range(len(vetor)):
        if (vetor[i] > elemento_maior[0]):
            elemento_maior = [vetor[i],i]
    return elemento_maior


def localiza_menor(vetor):
    elemento_menor = [vetor[0],0]
    for i in range(len(vetor)):
        if (vetor[i] < elemento_menor[0]):
            elemento_menor = [vetor[i],i]
    return elemento_menor


main()