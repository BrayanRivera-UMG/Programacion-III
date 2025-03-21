# Tarea 03 Árbol Binario de Búsqueda (ABB)
## Brayan Kenet Rivera Quinilla 
## 9490-23-2835

### Uso del menu
> [!CAUTION]
> Solo se permiten ingresar datos enteros

1. Insertar valor:
    - Permite ingresar numeros para empezar o agregar mas nodos al arbol

> [!NOTE]
> Solo se permiten ingresar datos enteros
2. Buscar valor
    - Busca un valor que se encuentre en el arbol y devuelve `True` si lo encuentra

> [!NOTE]
> Aplica 1 de los 3 casos de las reglas: nodo hoja, nodo con un solo hijo, nodo con dos hijos
3. Eliminar valor
    - Se tiene una funcion auxiliar para eliminar recursivamente, aplicando los 3 casos de las reglas de ABB

> [!IMPORTANT]
> Al momento de copiar la ruta, poner nombre de archivo con su respectiva extencion `.CSV`
4. Cargar desde archivo CSV
    - En este caso, el archivo lo tenia en el escritorio: `C:\Users\bkriv\Desktop`, luego de esto pongo el nombre del archivo: `numeros_100`, para despues poner su extencion: `.csv`. tendria que quedar algo asi: `C:\User\bkriv\Desktop\numeros_100.csv`, para que el programa lo encuentre y pueda leer los datos y armar el arbol para su posterior visualizacion

> [!NOTE]
> Hace el recorrido en InOrden
5. Convertir a binario
    - Convierte el arbol a una representacion binaria `InOrden`

> [!NOTE]
> Da una visualizacion del arbol
6. Mostrar arbol
    - Muestra la visualizacion del arbol si hubo algun tipo de cambio
    - No volvera a mostrar el arbol si no se le ha hecho algun tipo de cambio

> [!CAUTION]
> Da la opcion de borrar por completo el arbol
7. Deja borrar todo el arbol, presionando `s` que si quiere borrar o `n` que no se quiere borrar

> [!NOTE]
> Cierra el programa
8. Salir


# 1. Clases y Funciones
- Representa un nodo en el arbol con los siguientes atributos:
- Tiene dos Punteros `izquierda` y `derecha`, que apuntan a sus subarboles respectivos
  
```Python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
```
# 2. Clase: ArbolBinarioBusqueda
- Administra el arbol y sus operaciones
- La raiz (`self.raiz`) es el punto de inicio
  
  ```Python
  class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
  ```
### Metodos Principales
#### Insertar un valor
- Si el arbol esta vacio, el nuevo valor se convierte en la raiz
- si ya hay nodos, se colo en la posicion correcta segun la reglas del ABB
  
  ```Python
  def insertar(self, valor):
    if self.raiz is None:
        self.raiz = Nodo(valor)
    else:
        self._insertar_recursivo(self.raiz, valor)
  ```
#### Buscar un valor
- Se recorre el arbol siguiendo las reglas de ABB
- Si el valor buscado es menor, se revisa el subarbol izquierdo, y si es mayor, el derecho
  
  ```Python
  def buscar(self, valor):
    return self._buscar_recursivo(self.raiz, valor)
  ```
#### Eliminar un valor
+ Hay tres casos:
    + El nodo es una hoja (sin hijos)
    + el nodo tiene un solo hijo
    + el nodo tiene dos hijos (se reemplaza con el menor del subarbol derecho)

  ```Python
  def eliminar(self, valor):
    self.raiz = self._eliminar_recursivo(self.raiz, valor)
  ```
#### Cargar desde un archivo .CSV
- Lee un archivo CSV con numeros y los inserta en el arbol
  
  ```Python
  def cargar_desde_csv(self, ruta_archivo):
    with open(ruta_archivo, newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            self.insertar(int(fila[0]))
  ```
#### Generar visualizacion del arbol
- Genera una imagen del arbol
  
  ```Python
  def generar_visualizacion(self):
    dot = graphviz.Digraph()
    self._generar_dot(self.raiz, dot)
    dot.render("arbol_binario", format='pdf', view=True)
  ```
  
#### Borrar Arbol
- Borra por completo el arbol y deja vacio el espacio para crear otro arbol desde cero
  
  ```Python
  def borrar_arbol(self):
        self.raiz = None
        self.visualizacion_pendiente = True
        return True
  ```

### Funciones del Menu
- Limpieza de pantalla
  
  ```Python
  def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
  ```
- Menu principal
  
  ```Python
  def menu_principal():
    arbol = ArbolBinarioBusqueda()
    while True:
        print("\n--- Menú Árbol Binario de Búsqueda ---")
        print("1. Insertar valor")
        print("2. Buscar valor")
        print("3. Eliminar valor")
        print("4. Cargar desde archivo CSV")
        print("5. Convertir a binario")
        print("6. Mostrar visualización")
        print("7. Borrar todo el árbol")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "8":
            break
  ```  
