# Tarea 05 Árbol B
## Brayan Kenet Rivera Quinilla  
## 9490-23-2835

### Uso del menú
> [!CAUTION]
> Solo se permiten ingresar datos enteros

1. Insertar valor:
   - Permite agregar números al Árbol B.
   - Si el nodo está lleno, se divide según el grado especificado al iniciar.

> [!NOTE]
> Solo se permiten ingresar datos enteros.
2. Buscar valor:
   - Permite ingresar un valor y verifica si existe en el Árbol B.

> [!IMPORTANT]
> Al momento de copiar la ruta, poner nombre de archivo con su respectiva extensión `.CSV`
3. Cargar desde archivo CSV:
   - Ejemplo de ruta: `C:\Users\bkriv\Desktop\Ejercicio01.csv`.
   - El programa leerá los datos e insertará cada valor en el árbol.

> [!NOTE]
> Genera un archivo .gv y lo renderiza automáticamente en formato visual.
4. Mostrar Árbol:
   - Usa Graphviz para representar gráficamente el Árbol B actual.

> [!CAUTION]
> Borra todo el contenido del árbol y reinicia el grado.
5. Reiniciar Árbol con nuevo grado:
   - Pide un nuevo grado (entero >= 2).
   - El árbol actual se elimina y se crea uno nuevo con ese grado.

> [!NOTE]
> Cierra el programa.
6. Salir

---

# 1. Clases y Funciones

## Clase `BNode`
- Representa un nodo del Árbol B.
- Tiene atributos para los valores, hijos y si es hoja.
```python
class BNode:
    def __init__(self, grado, hoja=False):
        self.grado = grado
        self.hoja = hoja
        self.valores = []
        self.hijos = []
```

---

## Clase `BTree`
- Implementa la lógica del Árbol B: inserción, búsqueda, visualización y carga desde CSV.
```python
class BTree:
    def __init__(self, grado):
        self.raiz = BNode(grado, True)
        self.grado = grado
```

### Método: Insertar
```python
def insertar(self, valor):
    raiz = self.raiz
    if len(raiz.valores) == (2 * self.grado) - 1:
        nueva_raiz = BNode(self.grado, False)
        nueva_raiz.hijos.append(raiz)
        self._dividir_hijo(nueva_raiz, 0)
        self._insertar_no_lleno(nueva_raiz, valor)
        self.raiz = nueva_raiz
    else:
        self._insertar_no_lleno(raiz, valor)
```

### Método: Buscar
```python
def buscar(self, nodo, valor):
    i = 0
    while i < len(nodo.valores) and valor > nodo.valores[i]:
        i += 1
    if i < len(nodo.valores) and valor == nodo.valores[i]:
        return True
    if nodo.hoja:
        return False
    return self.buscar(nodo.hijos[i], valor)
```

### Método: Dividir Hijo
```python
def _dividir_hijo(self, padre, i):
    grado = self.grado
    hijo = padre.hijos[i]
    nuevo = BNode(grado, hijo.hoja)
    padre.hijos.insert(i + 1, nuevo)
    padre.valores.insert(i, hijo.valores[grado - 1])
    nuevo.valores = hijo.valores[grado:(2 * grado - 1)]
    hijo.valores = hijo.valores[0:grado - 1]
    if not hijo.hoja:
        nuevo.hijos = hijo.hijos[grado:(2 * grado)]
        hijo.hijos = hijo.hijos[0:grado]
```

### Método: Insertar en Nodo No Lleno
```python
def _insertar_no_lleno(self, nodo, valor):
    i = len(nodo.valores) - 1
    if nodo.hoja:
        nodo.valores.append(None)
        while i >= 0 and valor < nodo.valores[i]:
            nodo.valores[i + 1] = nodo.valores[i]
            i -= 1
        nodo.valores[i + 1] = valor
    else:
        while i >= 0 and valor < nodo.valores[i]:
            i -= 1
        i += 1
        if len(nodo.hijos[i].valores) == (2 * self.grado) - 1:
            self._dividir_hijo(nodo, i)
            if valor > nodo.valores[i]:
                i += 1
        self._insertar_no_lleno(nodo.hijos[i], valor)
```

---

### Visualización con Graphviz
- Crea un archivo `.gv` con el árbol y lo convierte a imagen.
```python
def graficar(self):
    dot = graphviz.Digraph()
    self._graficar_recursivo(self.raiz, dot)
    dot.render("arbol_b", view=True)

def _graficar_recursivo(self, nodo, dot, padre=None):
    nombre_nodo = str(id(nodo))
    etiqueta = "|".join(str(val) for val in nodo.valores)
    dot.node(nombre_nodo, etiqueta, shape='record')
    if padre:
        dot.edge(padre, nombre_nodo)
    for i, hijo in enumerate(nodo.hijos):
        self._graficar_recursivo(hijo, dot, nombre_nodo)
```

---

### Cargar desde archivo CSV
```python
def cargar_csv(self, ruta):
    try:
        with open(ruta, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            for fila in lector_csv:
                for valor in fila:
                    self.insertar(int(valor.strip()))
        print("Datos cargados exitosamente desde el archivo CSV.")
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique la ruta.")
```

---

# 2. Funciones del Menú

### Limpieza de pantalla
```python
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
```

---

### Menú principal
```python
def menu():
    grado = int(input("Ingrese el grado del árbol B (mayor o igual a 3): "))
    arbol = BTree(grado)
    while True:
        limpiar_pantalla()
        print("1. Insertar valor")
        print("2. Buscar valor")
        print("3. Cargar desde archivo CSV")
        print("4. Mostrar Árbol")
        print("5. Reiniciar Árbol con nuevo grado")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            valor = int(input("Ingrese un número: "))
            arbol.insertar(valor)
        elif opcion == '2':
            valor = int(input("Ingrese un número a buscar: "))
            encontrado = arbol.buscar(arbol.raiz, valor)
            print("Encontrado" if encontrado else "No encontrado")
            input("Presione Enter para continuar...")
        elif opcion == '3':
            ruta = input("Ingrese la ruta del archivo CSV: ")
            arbol.cargar_csv(ruta)
            input("Presione Enter para continuar...")
        elif opcion == '4':
            arbol.graficar()
            input("Presione Enter para continuar...")
        elif opcion == '5':
            grado = int(input("Ingrese el nuevo grado del árbol B: "))
            arbol = BTree(grado)
            print("Árbol reiniciado con nuevo grado.")
            input("Presione Enter para continuar...")
        elif opcion == '6':
            break
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")
```
