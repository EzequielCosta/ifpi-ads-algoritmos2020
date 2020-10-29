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
            print('Tela:', celular['tela'])
            print('Câmera Frontal:', celular['cam_frontal'])
            print(12 * '---')
    else:
        print("Sem dados")


def lista_vazia(lista):
    return bool(len(lista))

def verifica_input(palavra:str, tipo_palavra):
    # tipo_palavra = 'nume' -> numerico
    # tipo_palavra = 'word' -> palavra
    # tipo_palavra = 'nurd' -> alfanumerico

    if (tipo_palavra == "nume" and not(palavra.isnumeric()) ):
        return False
    elif (tipo_palavra == "word" and not(palavra.isalpha())):
        return False
    elif (tipo_palavra == "nurd" and not (palavra.isalnum())):
        return False

    return True

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



main()