# Uma determinada empresa armazena para cada funcionário uma ficha contendo o código,
# o número de horas trabalhadas e o seu nº de dependentes.  Considerando que a empresa
# paga R$ 12,00 por hora e R$ 40,00  por  dependentes  e  que  sobre  o  salário  são
# feitos  descontos  de  8,5%  para  o  INSS  e  5%  para  IR. Escreva  um algoritmoque
# leiao  código,  número  de  horas  trabalhadas  e  número  de  dependentes  de  N
# funcionários. Após a leitura de cada ficha, escreva os valores descontados para cada
# imposto e o salário líquido do funcionário


n = int(input("Digite a quantidade de funcinarios: "));

while n > 0:
    codigo = input("Digite o código do funcionário: ")
    num_horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
    num_dependentes = int(input("Digite o número de dependentes: "))

    salario_bruto = (12.0 * num_horas_trabalhadas) + (40 * num_dependentes)
    desconto_inss = salario_bruto * (8.5 / 100)
    desconto_ir = salario_bruto * (5 / 100)
    salario_liquido = salario_bruto - (desconto_ir + desconto_inss)

    print("""
    Para o funcionário de código {}, 
    o valor descontado para o imposto do INSS foi {:.2f}
    o valor descontado para o imposto do IR foi {:.2f}
    O salário líquido é : {:.2f}
    """.format(codigo,desconto_inss,desconto_ir,salario_liquido))