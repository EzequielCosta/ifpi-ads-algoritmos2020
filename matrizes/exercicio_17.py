# Leia uma matriz quadrada de ordem N e encontre a linha que possui a maior e a menor soma dos
# elementos.

def main():

    n = int(input("Digite a quantidade de colunas: "))
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append([])
            linha = int(input("Digite o valor da linha: "))
            matriz[i][j] = linha
    soma_colunas = soma_das_colunas(matriz)
    maior_soma = e_maior(soma_colunas)
    menor_soma = e_menor(soma_colunas)
    print("A maior linha é possui indice: ",maior_soma)
    print("A menor linha é possui indice: ", menor_soma)

def soma_das_colunas(matriz):
    soma = []
    for linha in matriz:
        count = 0
        for coluna in linha:
            count += coluna
        soma.append(count)
    return(soma)


def e_maior(soma_colunas):
    indice_maior = 0
    maior_valor = soma_colunas[0]

    for i in range(len(soma_colunas)):
        if (soma_colunas[i] > maior_valor):
            indice_maior = i
            maior_valor = soma_colunas[i]
    return indice_maior

def e_menor(soma_colunas):
    indice_menor = 0
    menor_valor = soma_colunas[0]

    for i in range(len(soma_colunas)):
        if (soma_colunas[i] < menor_valor):
            indice_menor = i
            menor_valor = soma_colunas[i]
    return indice_menor


main()