
def main ():

    palavra = input("Digite a palavra: ")
    numero = int(input("Digite a quantidade de palavras:  "))
    print(rotate_word(palavra,numero))


def rotate_word (palavra, numero):
    nova_palavra = ''
    for i in palavra:
        num_correspondente = ord(i)
        letra = chr(num_correspondente + numero)
        nova_palavra += letra
    return nova_palavra

main()