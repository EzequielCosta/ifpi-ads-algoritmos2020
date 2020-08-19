# Leia LimiteSuperior e LimiteInferior e escrevatodos 
# os números pares entre os limites lidos

limiteInferior = int(input("Digite o limite inferior: "));
limiteSuperior = int(input("Digite o limite superior: "));
resultado = limiteInferior + 1

while (resultado > limiteInferior and resultado < limiteSuperior):
    if (resultado % 2 != 0):
        print(resultado)
    resultado += 1;
    
