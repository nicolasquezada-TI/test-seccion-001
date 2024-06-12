#funcion sin parametro y sin retorno
#def (nom_funcion)():
def menu():
    espacio()#ejecutaria antes la funcion denominada "espacio"
    print("+++++M E N U+++++")
    print("")
    print("1.-Sumar")
    print("2.-Restar")
    print("3.-Multiplicar")
    print("4.-Dividir")
    print("")

def espacio():
    print("\n"*2)
    print("-.-.-.-.-.-.-.-.-.-.-.-")
          
#funcion sin parametro y con retorno
def suma1():
    total=4+5
    return total

#funcion con parametro y sin retorno
def sumar(a,b):
    tot=a+b
    print("El total es: ",tot)

#funcion con parametro y con retorno
def restar(a,b):
    tot=a-b
    return tot

################################################################################
while(True):
    menu()
    op = int(input("ingrese una opcion: "))
    if op==1:
        """
        t=suma1()
        print(t)
        print("el total es: ",suma1())#sin parametro y con retorno
        """
        numerito1=int(input("Ingrese numero 1: "))
        numeroto2=int(input("Ingrese numero 2: "))
        sumar(numerito1,numeroto2)
    elif op==2:
        numerito1=int(input("Ingrese numero 1: "))
        numeroto2=int(input("Ingrese numero 2: "))
        total=restar(numerito1,numeroto2)
        print("El total es: ",total)
