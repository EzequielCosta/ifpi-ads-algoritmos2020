# Um fazendeiro possui fichas de controle sobre sua boiada.
# Cada ficha contém numero de identificação, nome e peso (em kg) do boi.
# Escreva um algoritmoqueleiaos dados de N fichas e ao final, escrevao numero de identificação
# e o peso do boi mais magro e do boi mais gordo

n = int(input("Digite a quantidade de fichas: "))
print("")


num_identificacao = input("Digite o número de identificação: ")
nome = input("Digite o nome: ")
peso = float(input("Digite o peso: "))
print("")

peso_aux_maior = peso
num_identificacao_maior = num_identificacao
nome_maior = nome


peso_aux_menor = peso
num_identificacao_menor = num_identificacao
nome_menor = nome

while (n-1) > 0:

    num_identificacao = input("Digite o número de identificação: ")
    nome = input("Digite o nome: ")
    peso = float(input("Digite o peso: "))
    print("")

    if (peso > peso_aux_maior):
        peso_aux_maior = peso
        num_identificacao_maior = num_identificacao
        nome_maior = nome

    if (peso < peso_aux_menor):
        peso_aux_menor = peso
        num_identificacao_menor = num_identificacao
        nome_menor = nome

    n -= 1

print("O boi com identificação {0}, nome {1} e peso {2} possui o maior peso".format(num_identificacao_maior,nome_maior,peso_aux_maior))
print("O boi com identificação {0}, nome {1} e peso {2} possui o menor peso".format(num_identificacao_menor,nome_menor,peso_aux_menor))
#print(num_identificacao_maior)
#print(peso_aux_maior)
#print(nome_maior)
#print("")
#print(num_identificacao_menor)
#print(peso_aux_menor)
#print(nome_menor)