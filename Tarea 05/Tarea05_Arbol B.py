import csv
import os
import math
from graphviz import Digraph, nohtml

class NodoB:
    def __init__(self, grado, hoja=False):
        self.grado = grado
        self.hoja = hoja
        self.claves = []
        self.hijos = []

class ArbolB:
    def __init__(self, grado):
        self.grado = grado
        self.raiz = NodoB(grado, True)
        self.max_claves = grado - 1
        self.min_claves = math.ceil(grado / 2) - 1  # Modificado para trabajar con grados pares e impares

    def buscar(self, k, nodo=None):
        if nodo is None:
            nodo = self.raiz
        i = 0
        while i < len(nodo.claves) and k > nodo.claves[i]:
            i += 1
        if i < len(nodo.claves) and nodo.claves[i] == k:
            return True
        if nodo.hoja:
            return False
        return self.buscar(k, nodo.hijos[i])

    def insertar(self, k):
        r = self.raiz
        if len(r.claves) == self.max_claves:
            self._insertar_no_lleno(r, k)
            if len(r.claves) > self.max_claves:
                s = NodoB(self.grado, False)
                s.hijos.append(r)
                self._dividir_hijo(s, 0)
                self.raiz = s
        else:
            self._insertar_no_lleno(r, k)

    def _insertar_no_lleno(self, nodo, k):
        i = len(nodo.claves) - 1
        if nodo.hoja:
            nodo.claves.append(None)
            while i >= 0 and k < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1
            nodo.claves[i + 1] = k
        else:
            while i >= 0 and k < nodo.claves[i]:
                i -= 1
            i += 1
            self._insertar_no_lleno(nodo.hijos[i], k)
            if len(nodo.hijos[i].claves) > self.max_claves:
                self._dividir_hijo(nodo, i)

    def _dividir_hijo(self, padre, i):
        y = padre.hijos[i]
        z = NodoB(self.grado, y.hoja)
        # Cálculo del índice medio que funciona para grados pares e impares
        if self.grado % 2 == 0:  # Grado par
            medio = self.grado // 2 - 1
        else:  # Grado impar
            medio = self.grado // 2
        
        # Insertar la clave media en el padre
        padre.claves.insert(i, y.claves[medio])
        
        # Mover claves mayores al nuevo nodo
        z.claves = y.claves[medio + 1:]
        y.claves = y.claves[:medio]
        
        # Mover hijos si no es hoja
        if not y.hoja:
            z.hijos = y.hijos[medio + 1:]
            y.hijos = y.hijos[:medio + 1]
        
        # Insertar el nuevo nodo como hijo del padre
        padre.hijos.insert(i + 1, z)

    def cargar_desde_csv(self, archivo):
        with open(archivo, newline='') as f:
            lector = csv.reader(f)
            for fila in lector:
                for clave in fila:
                    if clave.strip().isdigit():
                        self.insertar(int(clave.strip()))

    def graficar(self, nombre_archivo="arbol_b"):
        dot = Digraph('BTree', filename=nombre_archivo,
                      node_attr={'shape': 'record', 'height': '.1'})
        self._graficar_nodo(self.raiz, dot)
        dot.view()
    
    def _graficar_nodo(self, nodo, dot):
        id_actual = f'node{id(nodo)}'
        etiquetas = []

        for i, clave in enumerate(nodo.claves):
            etiquetas.append(f'<f{i+1}>{clave}')
        etiquetas.insert(0, '<f0>')
        etiquetas.append(f'<f{len(nodo.claves)+1}>')

        etiqueta_final = '|'.join(etiquetas)
        dot.node(id_actual, nohtml(etiqueta_final))

        for i, hijo in enumerate(nodo.hijos):
            id_hijo = f'node{id(hijo)}'
            self._graficar_nodo(hijo, dot)
            dot.edge(f'{id_actual}:f{i}', f'{id_hijo}:f1')

    def borrar_todo(self):
        try:
            nuevo_grado = int(input("Ingrese el nuevo grado para el Árbol B: "))
            if nuevo_grado < 2:
                print("El grado debe ser al menos 2.")
                return
            self.grado = nuevo_grado
            self.raiz = NodoB(nuevo_grado, True)
            print("Árbol reiniciado con nuevo grado.")
        except ValueError:
            print("Entrada no válida. No se reinició el árbol.")

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def configurar_arbol():
    while True:
        try:
            grado = int(input("Ingrese el grado del Árbol B (mínimo 2): "))
            if grado >= 2:
                print(f"\n Árbol B configurado:")
                print(f"- Grado del árbol: {grado}")
                print(f"- Máximo de claves por nodo: {grado - 1}")
                print(f"- Mínimo de claves por nodo: {math.ceil(grado / 2) - 1}")
                return ArbolB(grado)
            else:
                print("El grado debe ser al menos 2.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

# --- MENÚ PRINCIPAL ---
def menu():
    print("<--- Configuración Inicial del Árbol B --->")
    arbol = configurar_arbol()
    while True:
        print("\n**** Menú Árbol B ****")
        print("1. Insertar número")
        print("2. Buscar número")
        print("3. Cargar desde CSV")
        print("4. Ver grafico del Arbol B")
        print("5. Borrar todo el arbol y cambiar el grado")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        limpiar_pantalla()
        if opcion == "1":
            try:
                clave = int(input("Ingrese el número a insertar: "))
                arbol.insertar(clave)
                print(f"Número: {clave}, insertado en el árbol.")
            except ValueError:
                print("Entrada inválida.")

        elif opcion == "2":
            try:
                clave = int(input("Ingrese el número a buscar: "))
                print("Número encontrado" if arbol.buscar(clave) else "Número no encontrado")
            except ValueError:
                print("Entrada inválida.")

        elif opcion == "3":
            ruta = input("Ingrese la ruta del archivo CSV: ")
            try:
                arbol.cargar_desde_csv(ruta)
                print("Carga exitosa")
            except Exception as e:
                print("Error al cargar el archivo: ", str(e))

        elif opcion == "4":
            arbol.graficar()
            print("Grafico generado")

        elif opcion == "5":
            confirmar = input("¿Está seguro que desea borrar el árbol y cambiar el grado? (s/n): ").lower()
            if confirmar == "s":
                arbol.borrar_todo()
            else:
                print("Operación cancelada.")

        elif opcion == "6":
            print("!!!Hasta Luego!!!...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()