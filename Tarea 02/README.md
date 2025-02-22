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
- #### Esta parte se divide en dos funciones 
### 4. Conversion de numeros romanos a decimales
### 5. Suma de numeros enteros
### 6. Limpiar la Pantalla
### 7. Menu Principal
