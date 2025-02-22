# Tarea 02 Recursividad
#### Brayan Kenet Rivera Quinilla
#### 9490-23-2835

### 1. Conversion a Binario
esta funcion convierte un numero entero a numero binario
- Explicacion:
  si el numero es menor que 2, lo devuelve como cadena, de lo contrario, divide el numero por 2 y concatena el residui, generando la representacion binaria
  ```Python
  def convertir_a_binario(numero):
    if numero < 2:
        return str(numero)
    return convertir_a_binario(numero // 2) + str(numero % 2)
  ```
### 2. Contar digitos de un numero
Cuenta la cantidad de digitos en un numero entero
- Explicacion:
  convierte el numero a positivo (si es negativo) y lo divide entre 10 hasta que quede un solo digito
  ```Python
  def contar_digitos(numero):
    numero = abs(numero)
    if numero < 10:
        return 1
    return 1 + contar_digitos(numero // 10)
  ```
### 3. Calculo de la raiz cuadrada entera
#### Esta parte se divide en dos funciones
- A. Usa una busquedda binaria para encontrar la raiz cuadrada entera del numero
  ```Python
  def calcular_raiz_cuadrada(numero, bajo, alto):
    if bajo > alto:
        return alto
    medio = (bajo + alto) // 2
    if medio * medio == numero:
        return medio
    elif medio * medio < numero:
        return calcular_raiz_cuadrada(numero, medio + 1, alto)
    else:
        return calcular_raiz_cuadrada(numero, bajo, medio - 1)

  ```
- B. verifica que el numero no sea negativo y llama a la funcion secundaria
  ```Python
  def raiz_cuadrada_entera(numero):
    if numero < 0:
        return "No se puede calcular la raiz cuadrada de un numero negativo"
    return calcular_raiz_cuadrada(numero, 0, numero)

  ```
### 4. Conversion de numeros romanos a decimales
- Explicacion:
  convierte un numero romano en decimal sumando o restando valores dependiendo del orden de los caracteres
  ```Python
  def convertir_a_decimal(numero_romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = 0
    for i in range(len(numero_romano)):
        if i == len(numero_romano) - 1 or valores[numero_romano[i]] >= valores[numero_romano[i + 1]]:
            resultado += valores[numero_romano[i]]
        else:
            resultado -= valores[numero_romano[i]]
    return resultado

  ```
### 5. Suma de numeros enteros
- Explicacion: suma todos los numero desde 1 hasta el numero ingresado
  ```Python
  def suma_numeros_enteros(numero):
    if numero <= 0:
        return 0
    return numero + suma_numeros_enteros(numero - 1)

  ```
### 6. Limpiar la Pantalla
- Explicacion: limpa la consola, al seleccionar una de las opciones
  ```Python
  def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
  
  ```
### 7. Menu Principal
- Explicacion: el menu permite al usuario elegir entre diferentes opcoine y ejecutar la funcion correspondiente. Despues de cada operacion, se limpia la pantalla y espera a que el usuario presione **ENTER** para volver al menu principal
  ```Python
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

        limpiar_pantalla()

        if opcion == "1":
            numero = int(input("Ingrese un numero entero: "))
            print("Conversion a numero Binario --> " + convertir_a_binario(numero))

        elif opcion == "2":
            numero = int(input("ingrese un numero entero: "))
            print(f"Cantidad de digitos: {contar_digitos(numero)}")

        elif opcion == "3":
            numero = int(input("Ingrese un numero positivo entero: "))
            print(f"Raiz cuadrada entera: {raiz_cuadrada_entera(numero)}")

        elif opcion == "4":
            romano = input("Ingrese un numero Romano: ")
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

        input("\n Presione ENTER para volver al Menu Principal...")

  ```
