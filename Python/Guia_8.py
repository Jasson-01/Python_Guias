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
def tieneMinuscula(contra:str) -> bool:
    valor:bool = False
    for i in contra:
        if (i >= 'a' and i <= 'z'):
            return True
    return valor 
#print(tieneMinuscula("tiene"))

def tieneMayuscula(contra:str) -> bool:
    valor:bool = False
    for i in contra:
        if (i >= 'A' and i <= 'Z'):
            return True
    return valor 
#print(tieneMayuscula("tieNe"))

def tieneNumeros(contra:str)->bool:
    valor: bool = False
    for i in contra:
        if (i >= '0' and i <= '9'):
            return True
    return valor 
#print(tieneNumeros("tieN9e"))

   
def fortaleza(contraseña:str)->str:
    if tieneNumeros(contraseña) and tieneMayuscula(contraseña) and tieneMinuscula(contraseña):
        return "VERDE"
    elif len(contraseña)<5:
        return "ROJA"
    else:
        return "AMARILLA"
           
print(fortaleza("horajh"))

# Problema 8 -------------------------------------

# saldoActual([("I",2000),("R",20),("R",1000),("I",300)]) -> int: reuslt = 1280
# lista[x][y]
def saldoActual(lista:[(str,int)])->int:
        ingresos: int = 0
        retiro: int = 0        
        for i in lista:
            if (i[0] == "I") :
                 ingresos += i[1]
            elif (i[0] == "R"):
                 retiro += i[1]
        return ingresos-retiro
print(saldoActual([("I",2000),("R",20),("R",1000),("I",300)]))  
                     
# Problema 9 -------------------------------------

####         
# def vocalesDistintas(palabra:str)->int: # me dice cuantas vocales distintas hay
#    contador:int = 0
#    for i in range(len(palabra)-1):
#        if palabra[i] != palabra[i+1]:
#           contador += 1    
#    return contador                    
#print(vocalesDistintas("abc"))                 
####

def vocales(palabra:str)->str: # De una palabra cualquiera me devuelve solo las vocales
       listaVocales:str = []
       for i in palabra:
           if i in "aeiouAEIOU":
               listaVocales.append(i)
       return listaVocales
#print(vocales("aetlpioo"))                        

def eliminarRepetidos(vocales:str)->str: # De un String de solo vocales me devuelve un String de vocales no repetidas 
    nueva:str = []
    for i in vocales:
        if i in nueva:
            None           
        #   print("esta vocal esta repetida",i)
        else:
           nueva.append(i)     
    return nueva
     
#print("eliminarRepetidos: ",eliminarRepetidos("nuevaa"))            

def tresVocalesDistintas(palabra:str)->bool:
    for i in palabra:
        if len(eliminarRepetidos(vocales(palabra))) >= 3 :
           return True
    return False
print(tresVocalesDistintas("palebre")) 
    
# ----------------------------------- Ejercicio 2 --------------------------

# Problema 1 ----------------------
#tipo InOut
def paresPorCeros(lista:[int])->None: # Esta funcion modifica el parametro modificado
    for i in range(0,len(lista),2):
        lista[i] = 0 

lista1 = [1,2,3,4,5]

#paresPorCeros(lista1)         
#print(lista1)    # -> devuelve [0,2,0,4,0]
print(paresPorCeros(lista1)) # -> devuelve None
print(paresPorCeros([1,2,4,5,6])) # -> devuelve None

# Problema 2 ---------------------
# tipo "in"

# def paresPorCeros2(lista:[int])->[int]: # Esta vez no modifico la lista original, devolviendo una nueva lista
#    nueva:[int] = []
#    for i in range(0,len(lista),1):
#        if i % 2 == 0:
#           nueva.append(0)
#    return nueva 
#nueva2 = [1,2,3,4,5]
#resultado = paresPorCeros2(nueva2)
#print(resultado)     


#############
def ceroEnPosPar2(x:list) -> list:
    y:list = x.copy()
    for elem in range(0,len(y),1):
        if elem % 2 == 0:
            y[elem] = 0
    return y

x2: list = [10,11,12,13,14,15]  # Almacena el resultado en otra lista
print(ceroEnPosPar2(x2)) # Muestra la lista con los ceros
print(x2)  # La lista original no se modifica

###############    
##### 1: 


def paresPorCeros4(lista: [int]) -> [int]:
    nueva = lista.copy()  # Crear una copia de la lista original
    for i in range(0, len(nueva), 2):
        nueva[i] = 0
    return nueva

nueva2 = [1, 2, 3, 4, 5]
resultado = paresPorCeros4(nueva2)  # Almacena el resultado en otra lista
print(nueva2)  # La lista original no se modifica
print(resultado)  # Muestra la lista con los ceros






###### 2:  Sin usar la funcion "copy()":


def paresPorCeros5(lista: [int]) -> [int]:
    nueva = lista[:]  # Crear una copia de la lista original 
    for i in range(0, len(nueva), 2):
        nueva[i] = 0
    return nueva

nueva2 = [1, 2, 3, 4, 5]
nueva2 = paresPorCeros5(nueva2)  # Almacena el resultado en la misma variable
print(nueva2)  # Muestra la lista con los ceros


# OBS: 

"""
La línea `nueva = lista[:]` crea una copia superficial de la lista `lista`. Esto significa que crea una nueva lista que contiene los mismos elementos que la lista original `lista`. La notación `[:]` se utiliza para copiar todos los elementos de la lista. 

Cuando realizas la asignación `nueva = lista[:]`, no estás copiando los elementos uno por uno, sino que estás creando una nueva lista que apunta a los mismos elementos de la lista original. Esto permite modificar la lista `nueva` sin afectar la lista original `lista`, lo que es útil cuando quieres trabajar con una copia de la lista sin cambiar la original.

Por ejemplo, si tienes una lista `lista = [1, 2, 3]` y luego haces `nueva = lista[:]`, obtendrás una nueva lista `nueva` que contiene los mismos elementos `[1, 2, 3]`. Si modificas `nueva`, como en el código de la función, no afectará a `lista`, y viceversa. Ambas listas son independientes.

Es una forma común de crear una copia de una lista en Python cuando deseas preservar la lista original.

"""


# Problema 3 ---------------------

def borraVocales(palabra:str)->str:
    vocales:str = []
    for i in palabra:
        if i in "aeiouAeiou":
            None 
        else:
           vocales.append(i)
    return vocales
print(borraVocales("palabra"))



# -------------------------- GIT 2DA FORMA:

def esVocal(letra:str) -> bool:
    vocales9 = ["a","e","i","o","u","A","E","I","O","U"]
    if pertenece5(vocales9, letra):
        return True
    return False

def pertenece5(a:list, n:int) -> bool:
    for i in range(0,len(a),1):
        if (a[i] == n):
            return True
    return False

def sinVocales9(cadena:str) -> str:
    cadena2: list = cadena.copy()
    for letra in cadena2:
        if esVocal(letra):
            cadena2.remove(letra)
    return cadena2

cadena = ["h","o","l","a"," ","c","o","m","o"]
print(sinVocales9(cadena))
print(cadena)

# Problema 4 ---------------------

def reemplazaVocales(palabra:[str])->[str]:
    nueva:str = []
    for i in palabra:
        if i in "aeiouAEIOU":
            nueva.append("_")
        else:
            nueva.append(i)
    return nueva 
print(reemplazaVocales("palabra"))         
       

# Problema 5 ---------------------

def daVueltaStr(palabra:str)->str:
    nueva2:str = []
    for i in range(len(palabra)): #Estoy tratando de iterar sobre los indices
        nueva2.append(palabra[len(palabra)-1-i])
    return nueva2 
print(daVueltaStr("palabra"))

# ----------------------------------- Ejercicio 3 --------------------------

# Problema 1 ------------------

# def listaDeEstudiantes(nombre:str)->[str]:
#    nueva3:str=[]
#    while nombre != "listo":
#        nueva3.append(nombre) 
#        if nombre == "listo":
#           break  
#    return nueva3

#valor = input("Ingrese nombre del estudiante: ")
#print(listaDeEstudiantes(valor))

# 1ER FORMA: 

def listaDeEstudiantes() -> [str]:
    nueva3 = []
    while True:
        nombre = input("Ingrese nombre del estudiante (o 'listo' para finalizar): ")
        if nombre == "listo":
            break
        nueva3.append(nombre)
    return nueva3

estudiantes = listaDeEstudiantes()
print("Lista de estudiantes ingresados:", estudiantes)

# 2DA FORMA: //

def listaDeEstudiantes9(nombre:str)->[str]:
    nueva9:[str]=[]
    while True: #El bucle while se ejecutará hasta que se ingrese la palabra "listo." Cuando se ingresa "listo," la condición nombre != "listo" se vuelve falsa, y la declaración break se ejecuta, lo que provoca la salida inmediata del bucle. Luego, el programa continúa con la instrucción return nueva3.
        nombre = input("Ingrese nombre del estudiante: ")
        if nombre == "listo":
            break
        nueva9.append(nombre) 
    return nueva9

print(listaDeEstudiantes9(""))

# Problema 2 ----------------

# def monederoSube(s:str)->tuple[(str,int)]:
#    historial: [(str,int)] = []
#    s = input("Digite el tramite que quiere hacer ("C","D") o "X" para finalizar: ")
#    if s == "C":

def computarCreditos(mov:str)->tuple[str,int]:
    cantidad:int= int(input("Ingrese cantidad: "))
    return (mov,cantidad)


def historialMonedero()->list[tuple[str,int]]:
    
    lista7:list[tuple[str,int]] = []
    movimiento: str = input("Ingrese movimiento: ") # necesitas pedir al usuario que ingrese un movimiento antes del bucle while para inicializar movimiento
    
    while (movimiento != "X") and  (movimiento != "x"):
        
        if (movimiento == "C") or (movimiento == "c"):
            lista7.append(computarCreditos(movimiento))
            
        elif (movimiento == "D") or (movimiento == "d"):
                lista7.append(computarCreditos(movimiento))
        movimiento = input("Ingrese movimiento: ") #para permitir al usuario ingresar múltiples movimientos.
        
    return lista7
print(historialMonedero())

# Problema 3 ----------------

import random

def getCarta()->int:
    return(random.randint(1,12))

def mainGame(secuenciaDeCartas)->int:
    print("bienvenido a 7 y medio, aquí tiene su primer carta ")
    carta: int = getCarta()
    suma: float
    decision: int
    secuenciaDeCartas.append(carta)

    if 0 < carta < 8:
        suma = carta
    else:
        suma = 0.5

    while suma < 7.5:
        print("su carta es",carta,"por ahora suma un total de",suma)
        decision = int(input("ingrese 1 para seguir jugando, 0 para plantarse"))
        if decision == 0:
            break
        carta=getCarta()
        secuenciaDeCartas.append(carta)
        suma+=carta
    print("su carta es",carta,"suma un total de",suma)

    if decision == 0:
        valorJugador: int = suma
        valorMaquina: int = suma + getCarta()
        if valorMaquina > 7.5:
            return 1
        if valorMaquina < 7.5:
            if valorJugador > valorMaquina:
                return 1
            return 0
        if valorMaquina == 7.5:
            return 0
        
    if suma > 7.5:
        return 0
    
    return 1

secuenciaDeCartas: list = []

if mainGame(secuenciaDeCartas) == 0:
    print("perdió el juego")
else:
    print("ganó el juego")

print(secuenciaDeCartas)


# ----------------------------------- Ejercicio 4 --------------------------
# Problema 1

def perteneceACadaUno(lista:[[int]],elemento:int)->[bool]:
    nueva:[bool]=[]
    for i in lista:
        if elemento in i:
            nueva.append(True)
        nueva.append(False)
    return nueva
lista = [[1,2],[3,4,5],[2,456,7,3],[1,2,87,3]]
print(perteneceACadaUno(lista,2))

# Problema 2 ------------------------------------

def esMatriz(s:[[int]])->bool:
    for i in s:
        if len(i) != s[0]: # compara las filas con la longitud de la primera fila
            return False  # Las filas no tienen la misma longitud.
    return True    
matriz = [[1,2],[3,4],[4,5]]
print(esMatriz(matriz))

# Problema 3 --------------------------------
# esMatriz -> no es necesario por Contrato!
# Ordenados
def filasOrdenadas(m:[[int]])->bool: # Tenemos una matriz de n dimensiones con cada lista dentro de ella ordenadas crecientes
    for i in m:
        if not ordenados(i):
            return False
    return True
print(filasOrdenadas([[1,2],[3,4],[9,5]]))
    


# Problema 4: elevarMatriz -----------------------------------------
import numpy as np

d: int = 2
m = np.random.random((d,d))**2
p: float = int(74)


def multiplicacion(m:list[list[float]]) -> list[list[float]]:
    filas: int = len(m)
    columnas: int = len(m[0])
    res: list[list[float]] = np.zeros((d, d)) #iniciar el res en 0


    for i in range(0,filas,1):
        for j in range(0,columnas,1):
            for k in range(0,columnas,1):
                res[i][j] += m[i][k] * m[k][j]

    return res

def elevarMatriz(m:list[list[float]],p:float) -> list[list[float]]:
    res = m

    for i in range(0,p-1):
        res = multiplicacion(m)
    return res





