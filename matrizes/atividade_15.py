#Leia uma matriz quadrada de ordem N e escreva se ela é ou não simétrica.
# Uma matriz quadrada é dita simétrica se A[i,j] =A[j,i].

def main():
    n = int(input("Digite a quantidade de colunas: "))
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append([])
            linha = int(input("Digite o valor da linha: "))
            matriz[i][j] = linha
    print("É simétrico: ",e_simetrica(matriz))


def e_simetrica(matriz):
    marca = True
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if (matriz[linha][coluna] != matriz[coluna][linha]):
                marca = False
                return marca
    return marca



main()