import sys

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

def main():
    try:    
        if(sys.argv[1] == "-s"):
            callback = sumar
        elif(sys.argv[1] == "-r"):
            callback = restar
        elif(sys.argv[1] == "-m"):
            callback = multiplicar
        elif(sys.argv[1] == "-d"):
            if(int(sys.argv[3])==0): 
                print("no se puede dividir entre 0")
                return 0
            callback = dividir
        print(callback(int(sys.argv[2]), int(sys.argv[3])))
    except IndexError:
        print("Uso en windows: ./operaciones.py -operacion numero1 numero2")

if __name__ == '__main__': #esto para q, si importo elarchivo, pueda llamar las funciones sin ejecutart todo
    main()