# Em uma eleição presidencial existem 3 (três)candidatos.
# Os votos são informados através de códigos. Os dados utilizados para a contagem dos votos
# obedecem à seguinte codificação:
# ·1, 2, 3 = voto para os respectivos candidatos;
# ·9 = voto nulo;
# ·0 = voto em branco;
# Escreva um algoritmo que leia o código votado por N eleitores. Ao final, calcule e escreva:
# a)total de votos para cada candidato;
# b)total de votos nulos;
# c)total de votos em branco;d)quem venceu a eleição.

n = int(input("Digite o número de votos: "))
cadidato_1 = 0
cadidato_2 = 0
cadidato_3 = 0
nulo = 0
branco = 0

while n > 0:
    voto = int(input("Digite o número do voto: "))
    if (voto == 1):
        cadidato_1 += 1
    elif (voto == 2):
        cadidato_2 += 1
    elif (voto == 3):
        cadidato_3 += 1
    elif (voto == 9):
        nulo += 1
    elif (voto == 0):
        nulo += 1
    n -= 1

print("{0} votos forão para o canditado 1".format(cadidato_1))
print("{0} votos forão para o canditado 2".format(cadidato_2))
print("{0} votos forão para o canditado 3".format(cadidato_3))
print("{0} forão votos nulos  ".format(nulo))
print("{0} forão votos em branco  ".format(branco))
