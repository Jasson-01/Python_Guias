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
 
# Problema 2 -------------------------------------

def divideATodos(lista:list[int],numero:int)->bool:
    for i in lista:
        if i % numero != 0:
            return False
    return True
print(divideATodos([4,6,8],5))


# Problema 3 -------------------------------------

def sumaTotal(s:[int]) -> int:
    valor = 0
    for i in s:
        valor = valor + i
    return valor

print(sumaTotal([1,2,3]))

# Problema 4 -------------------------------------

def ordenados(s:[int])->bool:
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] > s[j]:
               return False
    return True
print(ordenados([1,2,3,4,5]))
        
 
# Problema 5 -------------------------------------
     
def palabraMayorA7(s:[str]) -> bool:
    for i in s:
        if len(i) > 7:        
           return True
    return False 
print(palabraMayorA7(["hola","chau","adios","mayor"])) 

# Si "len()" estaria en codigo seria:
def longitud(objeto):
    contador = 0
    for i in objeto:
#        print(i)
        contador += 1
    return contador
print(longitud("palabra"))    

# Problema 6 -------------------------------------

# Usando While:

def esPalindroma(n:str)->bool:
    i = 0
    j = len(n) - 1
    while i < j:
        if n[i] != n[j]:
           return False
        i = i + 1
        j = j - 1
    return True
print(esPalindroma("ANA")) 

# Usando FOR:
  
def esPalindroma2(n:str)->bool:
        length = len(n)
        for i in range(length // 2):  # Iterar hasta la mitad de la cadena
            if n[i] != n[length - 1 - i]:  # Comparar caracteres simétricos
# Lo que hace esta expresión es acceder a los caracteres de la cadena de manera simétrica. Por ejemplo, si i es 0 (el primer carácter), n[length - 1 - i] accederá al último carácter de la cadena. Si i es 1 (el segundo carácter), accederá al penúltimo carácter, y así sucesivamente. De esta manera, se comparan los caracteres simétricos desde el principio y el final de la cadena para verificar si la cadena es un palíndromo.                
               return False
        return True    
print(esPalindroma2("ana"))

# Si fuera un numero:

def esCapicua(numero):
    # Convertir el número en una cadena
    num_str = str(numero)
    
    # Longitud de la cadena
    length = len(num_str)
    
    for i in range(length // 2):
        if num_str[i] != num_str[length - 1 - i]:
            return False
    
    return True

# Ejemplo de uso
print(esCapicua(121))  # Debería imprimir True
print(esCapicua(12345))  # Debería imprimir False


#----- Este no funciona
# def esPalindroma(n:str)->bool:
#    for i in range(len(n)):
#        for j in range(len(n)-1):
#            if n[i] != n[j]:
#                return False
#    return True
#print(esPalindroma("anna"))    


# Problema 7 -------------------------------------
   
# def fortaleza(contraseña:str)->str:
#    if len(contraseña) > 8:
#       if  





