# ESTE IMPORT OS ES PARA CREAR UNA FUNCION Y LIMPIAR LA PANTALLA DE LA CONSOLA
import os

def convertir_a_binario(numero):
    if numero < 2:
        return str(numero)
    return convertir_a_binario(numero // 2) + str(numero % 2)

def contar_digitos(numero):
    numero = abs(numero)
    if numero < 10:
        return 1
    return 1 + contar_digitos(numero // 10)

#FUNCION SECUNDARIA PARA CALCULAR LA RAIZ CUADRADA
def calcular_raiz_cuadrada(numero, bajo, alto):
    if bajo > alto:
        return alto
    medio = (bajo + alto) // 2
    if medio * medio == numero :
        return medio
    elif medio * medio < numero:
        return calcular_raiz_cuadrada(numero, medio + 1, alto)
    else:
        return calcular_raiz_cuadrada(numero, bajo, medio - 1)

#FUNCION PRINCIPAL PARA CALCULAR LA RAIZ CUADRADA
def raiz_cuadrada_entera(numero):
    if numero < 0:
        return "No se puede calcular la raiz cuadrada de un numero negativo"
    return calcular_raiz_cuadrada(numero, 0, numero)

#FUNCION PARA VERIFICAR LOS CARACTERES VALIDOS EN NUMEROS ROMANOS
def es_numero_romano_valido(numero):
    caracateres_validos = set('IVXLCDM')
    #AQUI SE VERIFICA QUE SOLO TENGA LOS CARACTERES VALIDOS
    if not all(c in caracateres_validos for c in numero):
        return False
    #AQUI VERIFICA QUE NO HAYA MAS DE 3 CARACTERES IGUALES O CONSECUTIVOS
    for i in range(len(numero) -3):
        if numero[i] == numero[i+1] == numero[i+2] == numero[i+3]:
            return False
    return True

def convertir_a_decimal(numero_romano):
    #VALORES DE LOS NUMERO ROMANOS
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    
    resultado = 0
    for i in range(len(numero_romano)):
        #SI EL ULTIMO NUMERO O EL ACTUAL ES MAYOR/IGUAL AL SIGUIENTE
        if i == len(numero_romano) - 1 or \
        valores[numero_romano[i]] >= valores[numero_romano[i + 1]]:
            resultado += valores[numero_romano[i]]
        else:
            resultado -= valores[numero_romano[i]]

    return resultado

def suma_numeros_enteros(numero):
    if numero <= 0:
        return 0
    return numero + suma_numeros_enteros(numero - 1)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
# MENU
def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Convertir a Binario")
        print("2. Contar Digitos")
        print("3. Raiz Cuadrada Entera")
        print("4. Convertir a Decimal desde Romano")
        print("5. Suma de Numero Enteros")
        print("6. Salir")
        opcion = input("Seleccione una opcion: ")

        limpiar_pantalla() # AQUI SE SUPONE QUE LIMPIA LA PANTALLA LUEGO DE SELECCIONAR UNA OPCION

        if opcion == "1":
            numero = int(input("Ingrese un numero entero: "))
            print("Conversion a numero Binario --> " + convertir_a_binario(numero))
        
        elif opcion == "2":
            numero = int(input("ingrese un numero entero: "))
            print(f"Cantidad de digitos: {contar_digitos(numero)}")

        elif opcion == "3":
            numero = int(input("Ingrese un numero positivo entero para calcular su raiz cuadrada: "))
            print(f"Raiz cuadrada entera: {raiz_cuadrada_entera(numero)}")

        elif opcion == "4":
            romano = input("Ingrese un numero Romano (I,V,X,L,C,D,M): ")
            print(f"Conversion a Numero Decimal --> {convertir_a_decimal(romano)}")
            
        elif opcion == "5":
            numero = int(input("Ingrese un numero positivo: "))
            if numero < 0:
                print("Debe de ingresar un numero positivo.")
            else:
                print(f"Suma de numero enteros hasta {numero}: {suma_numeros_enteros(numero)}")
            
        elif opcion == "6":
            print("!!! HASTA LUEGO !!!")
            break
        else:
            print("OPCION NO VALIDA, INTENTE DE NUEVO...")
            
        #SE ESPERA A PRESIONAR ENTER PARA REGRESAR AL MENU
        input("\n Presione ENTER para volver al Menu Principal...")
        
if __name__ == "__main__":
    menu()