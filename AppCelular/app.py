import json,os

def main():

    nome_arquivo = "banco.bd"

    #pega do banco de dados
    celulares = carrega_celulares(nome_arquivo)
    if (celulares == False):
        print("O arquivo não existe")
        quit()



    menu = tela_principal()

    opcao = 1

    while True :
        try:
            opcao = int(input(menu))
            if (opcao == 0):
                break
            elif (opcao == 1):
                celular = add_celulares()
                if (celular == False):
                    print("\nVocê digitou algum dado errado!\n")
                    continue
                celulares.append(celular)
                print('Celular cadastrado com sucesso!')
            elif (opcao == 2):
                lista_celular(celulares)
            elif (opcao == 3):
                buscar_celular(celulares)
            else:
                print("\nVocê digitou uma opção errada!\n")
                continue
            input("<enter> para continuar\n")
        except:
            print("\nEntrada Incorreta\n")
            continue


    fecha_conexao(nome_arquivo, celulares)



def tela_principal():

    menu = '***** App Jobs Cell *****\n'
    menu += '1 - Novo celular\n'
    menu += '2 - Listar celulares\n'
    menu += '3 - Buscar celulares\n'
    menu += '0 - sair\n'
    menu += '\nopcao >>> '

    return menu


def carrega_celulares(arquivo):

    #celulares = []

    if (os.path.exists(arquivo)):
        file = open(arquivo)
        celulares = json.loads(file.readline())
        file.close()
        return celulares
    else:
        return False


def add_celulares():
    print("Adicionar  celular\n")

    try:
        nome = input("Nome: ")
        if (not(is_alfanumerica(nome))):
            return False
        marca = input("Marca: ")
        if (not(is_alfanumerica(marca))):
            return False
        tela = input("Tela (polegadas): ")
        if (not (is_numero(tela))):
            return False
        valor = float(input('Valor (R$): '))
        cam_frontal = input('Camera frontal(sim/nao): ')
        if (not(is_letra(cam_frontal)) or (cam_frontal != 'sim' and cam_frontal != 'nao')):
            return False

        celular = {}
        celular["nome"] = nome
        celular["marca"] = marca
        celular["tela"] = tela
        celular["valor"] = valor
        celular["cam_frontal"] = cam_frontal

        return celular
    except:
        return False



def lista_celular(celulares):
    print("Existem {0} celular(res)\n".format(len(celulares)))
    if (len(celulares) > 0):
        for celular in celulares:
            print('Nome:', celular['nome'])
            print('Marca:', celular['marca'])
            print('Valor:', celular['valor'])
            print(12 * '---')
    else:
        print("Sem dados")


def fecha_conexao(nome_arquivo, celulares):
    dados = json.dumps(celulares)

    arquivo = open(nome_arquivo, 'w')
    arquivo.write(dados)
    arquivo.close()


def is_letra(palavra):
    for letra in palavra:
        if not(letra.isalpha() or letra.isspace()):
            return False
    return True


def is_alfanumerica(palavra):
    for letra in palavra:
        if not(letra.isalpha() or letra.isspace() or letra.isnumeric()):
            return False
    return True


def is_numero(palavra):
    try:
        float(palavra)
        return True
    except:
        return False


def buscar_celular(celulares):
    cont = 0
    buscar = input("Busque pelo o nome ou marca: ")
    for indice in range(len(celulares)):
        if ((buscar in (celulares[indice]["nome"]).lower()) or (buscar in (celulares[indice]["marca"]).lower()) ):
            print('ID: ', indice)
            print('Nome: ', celulares[indice]['nome'])
            print('Marca: ', celulares[indice]['marca'])
            print(12 * '---')
            cont = 1

    if (cont == 1):

        id = int(input("\nDigite o ID do celular selecionado: "))
        celular_selecionado = celulares[id]
        menu = "Escolha a opção:\n\n"
        menu += "1-Mostrar detalhes\n"
        menu += "2-Remover celular\n"
        menu += "3-Editar Celular\n"
        menu += "4-Duplicar registro\n"
        print(menu)

        opcao = int(input("Digite a opção: "))

        if (opcao == 1):
            mostrar_detalhe(celular_selecionado)
            print('\n')
        elif (opcao == 2):
            celulares = remover_celular(celulares,id)
            print("Removido com sucesso!\n")
        elif (opcao == 3):
            resultado = editar_celular(celulares,id)
            if(resultado):
                celulares = resultado
                print("Editado com sucesso")
            else:
                print("Não foi possível alterar")
        elif (opcao == 4):
            celulares = duplicar_celular(celular_selecionado,celulares)
            print("Duplicado com sucesso")


def mostrar_detalhe(celular_selecionado):

    print('Nome: ', celular_selecionado['nome'])
    print('Marca: ', celular_selecionado['marca'])
    print('Valor: ', celular_selecionado['valor'])
    print('Tela: ', celular_selecionado['tela'])
    print('Câmera Frontal: ', celular_selecionado['cam_frontal'])
    print('\n')

def remover_celular(celulares,indice):
    celulares.pop(indice)
    return celulares


def editar_celular(celulares,indice):

    menu = "O que você deseja editar:\n\n"

    menu += "1-Nome\n"
    menu += "2-Marca\n"
    menu += "3-Valor\n"
    menu += "4-Tela\n"
    menu += "5-Câmera\n"
    print(menu)
    opcao = int(input("Digite a opção: "))

    if (opcao == 1):
        nome = input("Digite o novo nome: ")
        celulares[indice]["nome"] = nome
    elif (opcao == 2):
        marca = input("Digite a nova marca: ")
        celulares[indice]["marca"] = marca
    elif (opcao == 3):
        valor = input("Digite o novo valor: ")
        celulares[indice]["valor"] = valor
    elif (opcao == 4):
        tela = input("Digite o novo tamanho de tela: ")
        celulares[indice]["tela"] = tela
    elif (opcao == 5):
        camera =  input("Digite se possui camera (sim/nao): ")
        if (camera == 'sim' or camera == 'nao'):
            celulares[indice]["cam_frontal"] = camera
    else:
        opcao = 0
    if (opcao != 0):
        return celulares
    else:
        return 0


def duplicar_celular(celular_selecionado,celulares):
    celulares.append(celular_selecionado)
    return celulares




main()