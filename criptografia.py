def main():
    n = int(input(""))

    for i in range(n):
        # PRIMEIRO PASSO
        palavra = input("")
        palavra_nova = desloca(palavra,3)
        
        # SEGUNDO PASSO
        palavra_invertida = inverte_palavra(palavra_nova)
        palavra_primeira_metade = palavra_invertida[:int(len(palavra_invertida) / 2)]

        # TERCEIRO PASSO
        palavra_metade = palavra_invertida[int(len(palavra_invertida) / 2):len(palavra_invertida)]
        palavra_segunda_metade = desloca(palavra_metade,-1,0)
        print(palavra_primeira_metade + palavra_segunda_metade)

def desloca(palavra,distancia, considerar_letra = True):
    nova_palavra = ''
    if (considerar_letra):
        for letra in palavra:
            if (letra.isalpha()):
                nova_palavra += chr(ord(letra) + distancia)

            else:
                nova_palavra += letra
        return nova_palavra
    elif (considerar_letra == False):
        for letra in palavra:
            nova_palavra += chr(ord(letra) + distancia)
        return nova_palavra

def inverte_palavra(palavra):
    nova_palavra = '';
    for i in range((len(palavra)-1),-1,-1):
        nova_palavra += palavra[i];
    return nova_palavra

main()
