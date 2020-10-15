def main():
    n = int(input("Digite a quantidade de colunas: "))
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append([])
            linha = int(input("Digite o valor da linha: "))
            matriz[i][j] = linha

    diagonal_principal = localiza_elemento_diagonal_principal(matriz)
    diagonal_secundaria = localiza_elemento_diagonal_secundaria(matriz)
    print("A soma dos elementos da diagonal principal é: ",diagonal_principal[1])
    print("A soma dos elementos da diagonal secundária é: ", diagonal_secundaria[1])
    print("A soma dos elementos que não estão nas diagonais é: ",remove_elementos(matriz))


def localiza_elemento_diagonal_principal(matriz):
    elementos_diagonal_principal = []
    soma = 0
    indices = []
    for i in range(len(matriz)):
        #elementos_diagonal_principal.append([i,matriz[i][i]])
        soma += matriz[i][i]
        indices.append([i,i])
    return [indices,soma]

def localiza_elemento_diagonal_secundaria(matriz):
    elementos_diagonal_secundaria = []
    soma = 0
    indices = []
    quant = len(matriz) -1
    for i in range(len(matriz)):
        elementos_diagonal_secundaria.append([[i,quant - i],matriz[i][quant - i]])
        indices.append([i,quant - i])
        soma += (matriz[i][quant - i])

    return [indices,soma]


def remove_elementos(matriz):
    elementos_diagonal_principal = localiza_elemento_diagonal_principal(matriz)
    elementos_diagonal_secundaria = localiza_elemento_diagonal_secundaria(matriz)

    elementos_uniao = elementos_diagonal_principal[0] + elementos_diagonal_secundaria[0]
    count = 0
    for i in elementos_uniao:
        matriz[i[0]][i[1]] = '';
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if (matriz[linha][coluna] == ''):
                continue
            else:
                count += matriz[coluna][linha]

    return (count)


main()





