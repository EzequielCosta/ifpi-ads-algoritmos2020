def main():

    n = int(input("Digite a quantidade de elementos do vetor: "))
    vetor = []
    count_elementos_iguais = 0

    for i in range(n):
        elemento = int(input("Digite o elemento: "))
        vetor.append(elemento)
        if( vetor.count(elemento) > 1):
            count_elementos_iguais += 1
    if (count_elementos_iguais > 0):
        print("O vetor possui elementos repetidos")

main()
