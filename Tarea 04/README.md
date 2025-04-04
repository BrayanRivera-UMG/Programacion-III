# Tarea 03 Árbol Binario de Búsqueda (AVL)
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
    - Busca un valor que se encuentre en el arbol
    - Si el valor no se encuentra en el arbol dara un mensaje que no se encuentra y regresara al menu

> [!NOTE]
> Aplica 1 de los 3 casos de las reglas: nodo hoja, nodo con un solo hijo, nodo con dos hijos
3. Eliminar valor
    - Ingrese algun valor que quiera eliminar del arbol
    - Si no esta ese valor dara un mensaje que el valor deseado no se encuentra en el arbol y regresara al menu

> [!IMPORTANT]
> Al momento de copiar la ruta, poner nombre de archivo con su respectiva extencion `.CSV`
4. Cargar desde archivo CSV
    - En este caso, el archivo lo tenia en el escritorio: `C:\Users\bkriv\Desktop`, luego de esto pongo el nombre del archivo: `Ejercicio1`, para despues poner su extencion: `.csv`. tendria que quedar algo asi: `C:\User\bkriv\Desktop\Ejercicio1.csv`, para que el programa lo encuentre, pueda leer los datos y armar el arbol para su posterior visualizacion

> [!NOTE]
> Da una visualizacion del arbol
5. Mostrar arbol
    - Muestra la visualizacion del arbol si hubo algun tipo de cambio
    - No volvera a mostrar el arbol si no se le ha hecho algun tipo de cambio

> [!CAUTION]
> Da la opcion de borrar por completo el arbol
6. Borrar todo el arbol
    - Deja borrar por completo el arbol
        - Presione `s` si se quiere borrar por completo el arbol
        - Presione `n` si no se quiere borrar el arbol por completo

> [!NOTE]
> Cierra el programa
7. Salir

# 1. Clases y Funciones
- Representa un nodo en el arbol con los siguientes atributos:
- Tiene dos Punteros `izquierda` y `derecha`, que apuntan a sus subarboles respectivos
- Tambien almacena la altura del nodo para balancear el arbol AVL
  
```Python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1
```

# 2. Clase: ArbolBinarioBusqueda
- Administra las operaciones basicas del ABB (insertar, buscar, eliminar)
- Contiene funciones para cargar desde CSV y generar visualizaciones

```Python
class ABB:
    def __init__(self):
        self.raiz = None
        self.visualizacion_pendiente = False
```

### Metodos Principales
#### Insertar un valor

```Python
def insertar(self, valor):
    if self.raiz is None:
        self.raiz = Nodo(valor)
    else:
        self._insertar_recursivo(self.raiz, valor)
    self.visualizacion_pendiente = True
```

### Buscar un valor
```Python
def buscar(self, valor):
    return self._buscar_recursivo(self.raiz, valor)
```

### Eliminar un valor
```Python
def eliminar(self, valor):
    self.raiz = self._eliminar_recursivo(self.raiz, valor)
    self.visualizacion_pendiente = True
```

### Cargar desde un archivo CSV
```Python
def cargar_desde_csv(self, ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            for valor in fila:
                self.insertar(int(valor.strip()))
```

### Visualizar el arbol con Graphviz
```Python
def generar_visualizacion(self):
        if self.raiz is None:
            return None
        dot = graphviz.Digraph('arbol_binario', filename='arbol_binario.gv',
                               node_attr={'color': 'lightblue2', 'style': 'filled'})
        dot.attr(size='8,8')

        def agregar_nodos_y_aristas(nodo):
            if nodo is None:
                return
            dot.node(str(nodo.valor), str(nodo.valor))
            if nodo.izquierda:
                dot.edge(str(nodo.valor), str(nodo.izquierda.valor))
                agregar_nodos_y_aristas(nodo.izquierda)
            if nodo.derecha:
                dot.edge(str(nodo.valor), str(nodo.derecha.valor))
                agregar_nodos_y_aristas(nodo.derecha)

        agregar_nodos_y_aristas(self.raiz)
        return dot
```
# 3. Clase: `AVL` (Extiende de ABB)
- Hereda del ABB, pero modifica los metodos `insertar` y `eliminar` para mantener el balance del arbol
- Implementa rotaciones (simple y doble)
```Python
class AVL(ABB):
    def insertar(self, valor):
        self.raiz = self._insertar_avl(self.raiz, valor)
        self.visualizacion_pendiente = True

    def eliminar(self, valor):
        self.raiz = self._eliminar_avl(self.raiz, valor)
        self.visualizacion_pendiente = True
```

# 4. Funciones del Menu
- Limpieza de pantalla
```Python
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
```

- Menu principal
```Python
def menu_principal():
    arbol = AVL()
    while True:
        print("\n--- MENÚ ÁRBOL AVL ---")
        print("1. Insertar valor")
        print("2. Buscar valor")
        ...
        print("8. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "8":
            break
```
