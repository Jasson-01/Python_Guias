# ----------------------------------- Ejercicio 1 --------------------------

# Problema 1

def pertenece(i: int, lista: list[int]) -> bool:
    if i in lista:
        return True
    else:
        return False

lista = [1,2,3]

resultado = pertenece(3, lista)

print(resultado)


# 2DA FORMA: 

def pertenece2(i: int, lista: list[int]) -> bool:
    return i in lista


# 3RA FORMA:

def pertenece3(i: int, lista: list[int]) -> bool:
    for elemento in lista:
        if elemento == i:
            return True
    return False

 # 4TA FORMA: (Tipos genericos)
 
def pertenece4(i: str, lista: str) -> bool: # En Python, el tipo "str" se utiliza tanto para cadenas de caracteres de longitud variable como para caracteres individuales, lo que simplifica el manejo de texto y caracteres en el lenguaje.
    for char in lista:
        if char == i:
            return True
    return False
print(pertenece4("d","abc"))
 
 
 
 
# Problema 2

def divideATodos(lista:list[int],numero:int)->bool:
    for i in lista:
        if i % numero != 0:
            return False
    return True
print(divideATodos([4,6,8],5))


