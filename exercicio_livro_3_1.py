def right_justify(s):
    tamanho = len(s)
    tamanho_espaco = 70 - tamanho
    return (tamanho_espaco * " " + s)

def main():
    print (right_justify("Day"))
        
main()
    