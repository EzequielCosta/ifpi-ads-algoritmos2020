def main():
    while True:
        print("""
        --------- Escolha a atividade que deseja excutar------------
        """);

        print("""
        1 - Exercicio 9.1
        2 - Exercicio 9.2
        3 - Exercicio 9.3
        4 - Exercicio 9.4
        5 - Exercicio 9.5
        6 - Exercicio 9.6
        """);

        numero_questao = input("Digite o numero da questão (Digite 0 para sair): ")
        arquivo = 'word.txt'
        if (numero_questao == '1'):
            palavra_acima_vinte(arquivo)
        elif (numero_questao == '2'):
            print("Palavras que não contem letra 'e'")
            print("")
            palavras_sem_letra_e(arquivo)
            palavra = input("Digite umaa palavra: ")
            print("Esta palavra possue a letra 'e': {0}".format(has_no_e(palavra)))
        elif (numero_questao == '3'):
            palavra = input("Digite uma palavra: ")
            n = int(input("Digite a quantidade de letras proibídas: "))
            print("A palavra {0} não usa nenhuma das palavras positivas: {1}".format(palavra,avoids(palavra,n)))
            print("")
            n = int(input("Digite a quantidade de letras proibídas: "))
            nao_contem_proibidas(arquivo,n)

        elif (numero_questao == '4'):
            palavra = input("Digite uma palavra: ")
            n = int(input("Digite a quantidade de letras: "))
            print("A palavra {0} apenas contém as letras inseridas: {1}".format(palavra,uses_only(palavra,n)))
        elif (numero_questao == '5'):
            palavra = input("Digite uma palavra: ")
            n = int(input("Digite a quantidade de letras: "))
            print("A palavra {0} contem as letras inseridas pelo menos uma vez: {1}".format(palavra,uses_all(palavra, n)))
        elif (numero_questao == '6'):
            palavra = input("Digite uma palavra: ")
            print("A palavra {0} está em ordem alfabética: {1}".format(palavra,is_abecedarian(palavra)))
            print("")
            print("Do arquivo word.txt, {0} estão em ordem alfabética".format(palavras_ordem_alfabetica(arquivo)))
        elif (numero_questao == '0' or int(numero_questao) > 6):
            print("Finalizando programa...")
            break


def palavra_acima_vinte(arquivo):

    arquivo = open(arquivo)
    palavras = arquivo.readlines()
    for palavra in palavras:
        palavra = palavra.strip()
        if (len(palavra) > 20):
            print(palavra)

def has_no_e (palavra):
    return not('e' not in palavra)


def palavras_sem_letra_e (arquivo):
    arquivo = open(arquivo)
    palavras = arquivo.readlines()
    palavras_sem_e = 0
    for palavra in palavras:
        palavra = palavra.strip()
        if ('e' not in palavra):
            print(palavra)
            palavras_sem_e += 1
    print('')
    print("De {0} palavras, {1} não possuem a letra 'e'".format(len(palavras),palavras_sem_e))


def avoids(palavra,quantidade_letras):
    letras = []
    for i in range(1,quantidade_letras+1):
        letras.append(input("Digite a {0}° letra proibida: ".format(i)))
    for j in letras:
        if (j in palavra):
            return False
    return True


def nao_contem_proibidas(arquivo,quantidade_letras):
    letras = []
    arquivo = open(arquivo)
    palavras = arquivo.readlines()
    contador = 0
    for i in range(1, quantidade_letras + 1):
        letras.append(input("Digite a {0}° letra proibida: ".format(i)))
    for j in palavras:
        j = j.strip()
        for z in letras:
            if (z in j):
                contador += 1
        if (contador == 0):
            print(j)
        contador = 0


def uses_only(palavra,quantidade_letras_obrigatorias):
    cont = 0
    letras_obrigatorias = []
    letras_repetidas = []
    letras_obrigatorias_copia = []
    for i in range(1,quantidade_letras_obrigatorias+1):
        letras_obrigatorias.append(input("Digite a {0}° letra obrigatória: ".format(i)))
    for j in palavra:
        if (j not in letras_obrigatorias):
           return False
    return True


def uses_all(palavra,quantidade_letras_obrigatorias):
    cont = 0
    letras_obrigatorias = []
    letras_obrigatorias_copia = []
    for i in range(1,quantidade_letras_obrigatorias+1):
        letras_obrigatorias.append(input("Digite a {0}° letra obrigatória: ".format(i)))
    for letra_obrigatoria in letras_obrigatorias:
        if (letra_obrigatoria in palavra):
            letras_obrigatorias_copia.append(letra_obrigatoria)
    if (letras_obrigatorias in letras_obrigatorias_copia):
        return True
    return False


def uses_all(palavra,quantidade_letras_obrigatorias):
    cont = 0
    letras_obrigatorias = []
    letras_repetidas = []
    letras_obrigatorias_copia = []
    for i in range(1,quantidade_letras_obrigatorias+1):
        letras_obrigatorias.append(input("Digite a {0}° letra obrigatória: ".format(i)))
    for j in palavra:
        if (j in letras_obrigatorias):
           letras_obrigatorias_copia.append(j)
    letras_obrigatorias_copia = list(set(letras_obrigatorias_copia))
    if (len(letras_obrigatorias_copia) == len(letras_obrigatorias)):
            return True
    return False

def is_abecedarian(palavra):
    ordem_alfabetica = ''
    maior = 96
    for letra in palavra:
        if (ord(letra) > maior):
            maior = ord(letra)
            ordem_alfabetica += letra
        elif (ord(letra) == maior):
            ordem_alfabetica += letra
    if (ordem_alfabetica == palavra):
        return True
    return False

def palavras_ordem_alfabetica(arquivo):
    arquivo = open(arquivo)
    palavras = arquivo.readlines()
    cont = 0
    for i in palavras:
        i = i.strip()
        if (is_abecedarian(i)):
            cont += 1
    return cont

main()