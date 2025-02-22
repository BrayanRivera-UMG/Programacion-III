# Tarea 02 Recursividad
#### Brayan Kenet Rivera Quinilla
#### 9490-23-2835

### 1. Conversion a Binario
esta funcion convierte un numero entero a numero binario
- Explicacion:
  Si el numero es menor que 2, lo devuelve como cadena, de lo contrario, divide el numero por 2 y concatena el residui, generando la representacion binaria
  ```Python
  def convertir_a_binario(numero):
    if numero < 2:
        return str(numero)
    return convertir_a_binario(numero // 2) + str(numero % 2)
  ```
### 2. Contar digitos de un numero
Cuenta la cantidad de digitos en un numero entero
- Explicacion:
  Convierte el numero a positivo (si es negativo) y lo divide entre 10 hasta que quede un solo digito
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
### 5. Suma de numeros enteros
### 6. Limpiar la Pantalla
### 7. Menu Principal
