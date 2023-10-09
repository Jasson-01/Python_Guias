# Problema 1

def raizDe2(x: int):
    raiz = x**0.5
    return raiz


print(round(raizDe2(5), 4))

# Problema 2


def imprimir_hola():
    saludo = "hola"
    return saludo


print(imprimir_hola())

# Problema 3


def imprimir_un_verso():
    letra = "¿Qué será? \n Tal ves' la noche como de costumbre \n Amanecerá \n Sigo pensando en tus gestos \n cuando se me cruza otra \n Pero es lo que hay \n ¿Y qué más da? Quiero olvidar,\n se va a lograr"
    return letra


print(imprimir_un_verso())

# Problema 4


def factorial():
    a = 2*1
    b = 3*a
    c = 4*b
    d = 5*c

    print("factorial de 2 es: ", a)
    print("factorial de 3 es: ", b)
    print("factorial de 4 es: ", c)
    print("factorial de 5 es: ", d)


print(factorial())

# ---------------------------------------- EJERCICIO 2 ------------------------------------

# Problema 1


def imprimir_saludo():
    saludo2 = input("Digite saludo: ")
    return saludo2


# saludo_ingresado = imprimir_saludo()

# print("Hola", saludo_ingresado)

# Problema 2


def raiz_cuadrada(numero: int) -> float:
    raiz2 = numero**0.5
    return raiz2


# evaluar = input("Digite numero: ")
# print(raiz_cuadrada(int(evaluar)))

# Problema 3


def imprimir_dos_veces():
    estribillo = "Bye \n Mejor sigue tu camino \n Mientras fumo y tomo vino \n Que estar contigo ya no me convino \n"
    return estribillo*2


print(imprimir_dos_veces())

# Problema 4


def es_multiplo_de(n: int, m: int):
    es_multiplo = n % m == 0
    return es_multiplo


print(es_multiplo_de(4, 2))

# Problema 5


def es_par(n: int):
    es_par2 = es_multiplo_de(n, 2)
    return es_par2


print(es_par(4))

# Problema 6

# esta funcion nos devuelve la cantidad de pizzas que dado un numero de comensales y la cantidad de porciones


def cantidad_de_pizzas(comensales, min_cant_de_porciones):

    porciones_totales = comensales * min_cant_de_porciones
    porciones_necesarias: float = porciones_totales / 8

    if (porciones_necesarias % 1 == 0):  # verifica si la div fue entera
        # las pizzas son exactas entonces no necesito agregar
        return (porciones_totales//8)
    else:
        # las pizzas no son exactas entonces agrego
        return (porciones_totales // 8) + 1


print(cantidad_de_pizzas(9, 2))


# ---------------------------------------- EJERCICIO 3 ------------------------------------


# Problema 1
def alguno_es_0(numero1, numero2):
    evaluar4 = numero1 == 0 or numero2 == 0
    return evaluar4


print(alguno_es_0(3, 9))

# Problema 2


def ambos_son_cero(numero1, numero2):
    evaluar5 = numero1 == 0 and numero2 == 0
    return evaluar5


print(ambos_son_cero(0, 0))

# Problema 3


def es_nombre_largo(nombre: str) -> bool:
    probando = len(nombre) >= 3 and len(nombre) <= 8
    return probando


print(es_nombre_largo("ju"))

# Problema 4


def es_bisiesto(año: int) -> bool:
   # result1 = (año % 400  == 0) and (año % 100  != 0)
   # result2 = (año % 4  == 0) and (año % 100  != 0)
   #  result4 = ((año % 400 == 0) or (año % 4 != 0)) and (año % 100 != 0)
   #  return result4

    result3 = (año % 400 == 0) or ((año % 4 == 0) and (año % 100 != 0))
    return result3


print(es_bisiesto(2004))

# ---------------------------------------- EJERCICIO 4 ------------------------------------

# Problema 1


def peso_pino(d: float) -> float:  # dado "d" metros me dice cual es el "peso del pino"
    if (0 <= d <= 3):
        peso: float = d*100*3
    else:
        peso: float = 900 + ((d-3)*200)
    return peso


# d: float = float(input("Ingrese altura del pino: "))
# print(peso_pino(d))

# Problema 2  # me dice si "peso del pino" es util o no


def es_peso_util(m: float) -> bool:
    if (400 <= m) and (m <= 1000):  # rango de 400 y 100 kilos
        return True
    else:
        return False


# m: float = float(input("Ingrese peso del pino: "))

# print(es_peso_util(m))

# Problema 3
# def sirve_pino()->bool: # (int="altura del pino") -> "bool:me dice si sirve o no"


def sirve_pino(h: float) -> bool:
    return es_peso_util(peso_pino(h))


# print(sirve_pino(2))

# ---------------------------------------- EJERCICIO 5 ------------------------------------

# Problema 1
def devolver_el_doble_si_es_par(n: int) -> int:
    if n % 2 == 0:
        return 2*n
    else:
        return n


print(devolver_el_doble_si_es_par(3))

# Problema 2


def devolver_valor_si_es_par_sino_el_que_sigue(n: int) -> int:
    if n % 2 == 0:
        return n
    else:
        return n+1


print(devolver_valor_si_es_par_sino_el_que_sigue(5))

# 2DA FORMA:


def devolver_valor_si_es_par_sino_el_que_sigue2(n: int) -> int:
    result = n if n % 2 == 0 else n+1
    return result


print(devolver_valor_si_es_par_sino_el_que_sigue2(3))

# Problema 3


def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n: int):
    if (n % 3 == 0) & (n % 9 != 0):
        return n*2
    elif (n % 9 == 0):
        return n*3
    else:
        return n


print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(9))

# Problema 4


def tamaño_nombre(m: str) -> str:
    if len(m) >= 5:
        return "Tu nombre tiene muchas letras"
    else:
        return "Tu nombre tiene menos de 5 caracteres"


print(tamaño_nombre("jason"))


# Problema 5

def eres_jubilado(sexo: str, años: int) -> str:
    if sexo == "M" or sexo == "m":
        if (años < 65) & (años > 18):
            return "Te toca trabajar"
        return "Anda de vacaciones"
    elif sexo == "F" or sexo == "f":
        if (años < 60) & (años > 18):
            return "Te toca trabajar"
        return "Anda de vacaciones"
    else:
        return "none"


print(eres_jubilado("m", 7))

# ---------------------------------------- EJERCICIO 6 ------------------------------------

# Usando While:

# Problema 1:


def del_1_al_10() -> int:
    n = 1
    while n <= 10:
        print(n)
        n = n + 1
  #  return n


# del_1_al_10()
# print(del_1_al_10())


def imprimir_del_1_al_10():
    numero = 1
    while numero <= 10:
        print(numero)
        numero += 1


# imprimir_del_1_al_10()

# Problema 2:


def pares_entre_10_al_40():
    numero = 10
    while (numero >= 10) & (numero <= 40):
        if numero % 2 == 0:
            print(numero)
        numero = numero + 1
    return numero


pares_entre_10_al_40()

# Problema 3:


def imprimir_10_eco():
    palabra: str = "eco"
    contador: int = 0
    while contador < 10:
        print(palabra)
        contador = contador + 1


imprimir_10_eco()


# Problema 4

def cuenta_regresiva(numero: int):
    while numero != 0:
        print(numero)
        numero = numero - 1
    print("Despegue!!")


cuenta_regresiva(7)

# Problema 5


def viaje_en_el_tiempo(añoi: int, añof: int):  # añof < añoi " al pasado "
    while añoi != añof:
        print("Viajo un año al pasado, estamos en el año: ", añoi)
        añoi = añoi - 1
    if añoi == añof:
        print("Viajo un año al pasado, estamos en el año: ", añoi)


viaje_en_el_tiempo(2023, 2020)

# Problema 6  ( -_- )


def monitoreo_ac(partida: int, llegada: int):
    if (llegada < 0):
        llegada += 1  # pues año 0 no existe
#    print("arrancamos en el año", partida)
    while (partida > llegada):
        if (partida > 0):
            #            print("viajo 20 años al pasado, estamos en el ", partida)
            #        else:
            if (partida >= llegada+20):  # pues si es menor y vuelvo a viajar 20 años me paso de destino
                print("viajo 20 años al pasado, estamos en el",
                      valor_abs(partida-1), "a.C")
            else:
                print("viajo", valor_abs(llegada-partida), "años",
                      "estamos en ", valor_abs(partida), "a.c")
        partida -= 20
#    print("llegamos a destino")


def valor_abs(x: int) -> int:
    if x < 0:
        return -x
    else:
        return x


# partida: int = int(input("ingrese partida "))
# llegada: int = int(input("ingrese llegada "))
# monitoreo_ac(partida, llegada)

# ---------------------------------------- EJERCICIO 7 ------------------------------------

# Implementar lasfunciones del ejercicio 6 utilizando for num in range(i,f,p):.Recordar que la funcion range para generar una secuencia de numeros en un rango dado,con un valor inicial i, un valor final f y un paso p.Ver documentacion: https://docs.python.org/es/3/library/stdtypes.html#typesseq-range


# Problema 6.1 :

def del_1_al_10_2() -> int:
    for i in range(1, 11):
        print(i)


del_1_al_10_2()

# Problema 6.2 :


def pares_entre_10_al_40_2():
    for i in range(10, 41, 2):
        print(i)


pares_entre_10_al_40_2()

# Problema 6.3:


def imprimir_10_eco_2():
    for i in range(1, 11):
        print("eco")


imprimir_10_eco_2()

# Problema 6.4


def cuenta_regresiva_2(numero: int):

    for i in range(numero, 0, -1):
        print(i)
    print("Despegue!!!")


evaluar = input("Digite comienzo de la cuenta regresiva: ")

cuenta_regresiva_2(int(evaluar))

# Problema 6.5:


def viaje_en_el_tiempo_2(añoi: int, añof: int):
    for i in range(añoi, añof-1, -1):
        print("Viajo un año al pasado, estamos en el año: ", i)


desde = int(input("Digite año actual: "))
hasta = int(input("Digite año al que quiere llegar: "))

viaje_en_el_tiempo_2(desde, hasta)
