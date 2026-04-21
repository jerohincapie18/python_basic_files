#En python, true, es con T mayuscula, como false con F, y los operadores logicos
# seral literalmente letras: and, or, no existen && ni ||
print(True and True)
print(True and False)
print(True or False)

# esta funcion define estrictametne los tipos de datos que va a manejar
def is_positive(n: int) -> bool:
    if n%2 == 0:
        return True
    else:
        return False

print(not(is_positive(2))-1) # true? lol 
print(False-1)
print(True == -1)