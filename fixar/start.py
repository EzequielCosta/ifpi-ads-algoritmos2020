def main():

    menu = '*** Brincando com Listas ***'
    menu += '\n 1 - Inserir Valores'
    menu += '\n 2 - Mostrar Valor posição'
    menu += '\n 3 - Remover do Final'
    menu += '\n 4 - Remover do Início'
    menu += '\n 5 - Remover de Posição Específica'
    menu += '\n 6 - Inserir valores em Posição Específica'
    menu += '\n 7 - Contagem de Números Pares'
    menu += '\n 8 - Contagem de Números Impares'
    menu += '\n 9 - Contagem de Números Primos'
    menu += '\n 10 - Contagem de Números Positivos'
    menu += '\n 11 - Contagem de Números Zerados'
    menu += '\n 12 - Média dos Valores'
    menu += '\n 13 - Contar ocorrências de um Dado Valor'
    menu += '\n 14 - Dobrar todos os valores'
    menu += '\n 15 - Dobrar valores múltiplos de N'
    menu += '\n 16 - Contagem de Números Negativos'
    menu += '\n 17 - Mostrar array'
    menu += '\n 0 - Sair '
    menu += '\n\n Opção >>> '

    lista = []

    while True:  # Condição sempre verdadeira, só irá para em caso de break ou error
        opcao = int(input(menu))

        # Verificar operacao a fazer de acordo com a opcao
        if opcao == 1:
            # Listas quando passadas como argumentos e modificadas por
            # funções não é necessário retorná-las
            # Se modificar a lista dentro de um função, as variáveis que já
            # apontavam para ela, terão acesso a lista moficiada normalmente
            # Por isso nao está ```lista = inserir_valores(lista)````
            inserir_valores(lista)
        elif opcao == 2:
            mostra_valor(lista)
        elif opcao == 3:
            remove_ultimo_elemento(lista)
        elif opcao == 4:
            remove_primeiro_elemento(lista)
        elif opcao == 5:
            remove_elemento(lista)
        elif opcao == 6:
            insere_em_posicao(lista)
        elif opcao == 7:
            contador_pares(lista)
        elif opcao == 8:
            contador_impar(lista)
        elif opcao == 9:
            contador_primo(lista)
        elif opcao == 10:
            contador_positivo(lista)
        elif opcao == 11:
            cont_zero(lista)
        elif opcao == 12:
            calcula_media(lista)
        elif opcao == 13:
            cont_ocorrencia_elemento(lista)
        elif opcao == 14:
            dobra_valores(lista)
        elif opcao == 15:
            dobra_valores_multiplos(lista)
        elif opcao == 16:
            contador_negativo(lista)
        elif opcao == 17:
            mostra_array(lista)
        elif opcao == 0:  # sair do while
            break
        else:
            print('Opção Inválida')


def inserir_valores(lista):
    qtd = int(input('Quantos valores desejar inserir?'))

    for i in range(qtd):
        valor = int(input('Valor: '))
        lista.append(valor)

    print('Valores inseridos com sucesso!')
    input('<enter> to continue...')


def mostra_valor(lista):
    posicao = int(input('Qual posição? '))
    print('Valor buscado:')
    print(lista[posicao])

    input('<enter> to continue...')

def remove_ultimo_elemento(lista):
    valor_deletado = lista[-1]
    lista.pop(-1)
    print('Valor {0} apagado com sucesso!'.format(valor_deletado))

    input('<enter> to continue...')

def remove_primeiro_elemento(lista):
    valor_deletado = lista[1]
    lista.pop(1)
    print('Valor {0} apagado com sucesso!'.format(valor_deletado))

    input('<enter> to continue...')

def remove_elemento(lista):
    posicao = int(input('Qual posição? '))
    valor = lista[posicao]
    lista.pop(posicao)
    print('Valor {0} removido com sucesso!'.format(valor))

    input('<enter> to continue...')

def insere_em_posicao(lista):
    posicao = int(input('Qual posição? '))
    valor = int(input('Qual o valor? '))
    lista[posicao] = valor
    print('Valor {0} foi inserido com sucesso!'.format(lista[posicao]))

    input('<enter> to continue...')

def contador_pares(lista):
    cont = 0
    for numero in lista:
        if (numero % 2 == 0 ):
            cont += 1
    print("{0} valores são pares".format(cont))

    input('<enter> to continue...')

def contador_impar(lista):
    cont = 0
    for numero in lista:
        if (numero % 2 != 0 ):
            cont += 1
    print("{0} valores são ímpares".format(cont))

    input('<enter> to continue...')

def contador_positivo(lista):
    cont = 0
    for numero in lista:
        if (numero > 0):
            cont += 1
    print("{0} valores são positivos".format(cont))

    input('<enter> to continue...')

def contador_negativo(lista):
    cont = 0
    for numero in lista:
        if (numero < 0):
            cont = + 1
    print("{0} valores são negativos".format(cont))

    input('<enter> to continue...')

def contador_primo(lista):
    cont = 0
    for numero in lista:
        if (verifica_primo(numero)):
            cont += 1
    print("{0} valores são primos".format(cont))

    input('<enter> to continue...')

def verifica_primo(numero):
    if ((numero != 0) and (numero != 1)):
        return False
    cont_divisores = 0
    for n in range(1, numero):
        if numero % n == 0:
            cont_divisores += 1
            if cont_divisores > 1:
                break
    # retorna 0 se o numero não for primo, se for, retorna 1
    if cont_divisores > 1:
        return 0
    return 1


def cont_zero(lista):
    cont = 0
    for numero in lista:
        if (numero == 0):
            cont += 1
    print("{0} valores são zeros".format(cont))

    input('<enter> to continue...')

def calcula_media(lista):
    soma = 0
    for numero in lista:
        soma += numero
    media = soma / (len(lista))
    print("A média é : {:.2f}".format(media))

    input('<enter> to continue...')

def cont_ocorrencia_elemento(lista):
    valor = int(input("Digite o valor: "))
    ocorrencia = lista.count(valor)
    print("O elemento apareceu {0} vezes".format(ocorrencia))

    input('<enter> to continue...')

def dobra_valores(lista):
    for index in range(len(lista)):
        lista[index] *= 2
    print("Valores dobrados com sucesso!")

    input('<enter> to continue...')

def dobra_valores_multiplos(lista):
    n = int(input("Dobrar os valores múltiplos de : "))
    for index in range(len(lista)):
        if (lista[index] % n == 0):
            lista[index] *= 2
    print("Valores múltiplos de {0} dobrados com sucesso!".format(n))

    input('<enter> to continue...')

def mostra_array(lista):
    print(lista)

    input('<enter> to continue...')


main()