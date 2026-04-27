#En un programa de Python estándar, la lista sys.argv contiene
#los argumentos de la línea de comandos de la manera estándar,
#guarda los string de forma seguida, tener '-s' es un espacio, y no guarda los espacios en blanco

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
        print(callback(int(sys.argv[2]), int(sys.argv[3])), ".Longitud de args de la command line:", len(sys.argv))
    except IndexError:
        print("Uso en windows: ./operaciones.py -operacion numero1 numero2", len(sys.argv))
        #len() indica la longitud de la cadena que pasa como argumento

if __name__ == '__main__': #esto para q, si importo elarchivo, pueda llamar las funciones sin ejecutart todo
    main()

#Cuando un archivo de Python se ejecuta directamente, la variable especial "__name__"
# se establece en "__main__". Por lo tanto, es común tener el código estándar if __name__ ==...
# que se muestra arriba para llamar a una función main() cuando el módulo se ejecuta directamente,
# pero no cuando otro módulo lo importa.
