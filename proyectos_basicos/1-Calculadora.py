# Link: https://youtu.be/M7qr5Tib9gw?si=qVkjQMxZdmfSHnzr&t=1059
#
# CONSIGNA:
"""
Consigna 1:
Ejercicio de operadores
Crea una calculadora
"""

# HISTORIA DE USUARIO
"""
-[x] se le muestra al usuario el texto de bienvenida y las opciones de operacion
-[x] el usuario ingresa la opcion
-[] dependiendo de la opcion elegida, el usuario ingresará 2 o más operandos
-[] se le muestra el resultado al usuario
"""
# CODIGO

## se le muestra al usuario el texto de bienvenida y las opciones de operacion
print("""CALCULADORA:""")
print("""seleccione la operacion que desea realizar""")
operaciones = ["suma", "resta", "multiplicacion", "division decimal", "division entera", "resto de division", "potencia", "raiz"]
i = 1
for operacion in operaciones:
    print(f"{i} - {operacion}")
    i += 1

# el usuario elige la operacion a realizar
n_operacion = int(input("escriba el nro de la opcion elegida: "))

# dependiendo de la opcion elegida, el usuario ingresará 2 o más operandos
if n_operacion > 4 :
    
    # el usuario ingresara solo 2 operandos
    while True :
        operandos = input("ingrese solo 2 numeros separados por un espacio: ")
        operandos = operandos.split(" ")
        
        for i in range(0, len(operandos)):
            operandos[i] = int(operandos[i])
            
        if len(operandos) <= 2 :
            break
else :
    # el usuario ingresará varios operandos
    operandos = input("ingrese varios numeros separados por un espacio: ")
    operandos = operandos.split(" ")
    for i, operando in enumerate(operandos):
        operandos[i] = int(operando)

# se realiza la operacion elegida con los operandos correspondientes
resultado, *operandos = operandos

if n_operacion == 1: # suma
    for i, numero in enumerate(operandos):
        resultado += int(numero)
elif n_operacion == 2: # resta
    for i, numero in enumerate(operandos):
        resultado -= int(numero)
elif n_operacion == 3: # multiplicacion
    for i, numero in enumerate(operandos):
        resultado *= int(numero)
elif n_operacion == 4: # division decimal 
    for i, numero in enumerate(operandos):
        resultado /= int(numero)
elif n_operacion == 5: # division entera
    for i, numero in enumerate(operandos):
        resultado //= int(numero)
elif n_operacion == 6: # resto de division
    for i, numero in enumerate(operandos):
        resultado %= int(numero)
elif n_operacion == 7: # potencia
    for i, numero in enumerate(operandos):
        resultado **= int(numero)
elif n_operacion == 8: # raiz
    for i, numero in enumerate(operandos):
        resultado **= 1/int(numero)
    
# se muestra el resultado
print(f"la {operaciones[n_operacion-1]} de los operandos ingresados es: {resultado}")

