
def linha_horizontal(tam):
    print ("+",("- " * tam),"+",("- " * tam),"+",("- " * tam),"+",("- " * tam),"+")
    

def linha_vertical(tam):
    print ("| " + " "*(2 * tam), "| " + " "*(2*tam),"|" + " "*(2*tam),"|" + " "*(2*tam),"|");

def main():
    
    tam = 4
    linha_horizontal(tam)
    linha_vertical(tam)
    linha_vertical(tam)
    linha_vertical(tam)
    linha_vertical(tam)
    linha_horizontal(tam)
    linha_vertical(tam)
    linha_vertical(tam)
    linha_vertical(tam)
    linha_vertical(tam)
    linha_horizontal(tam)


main()