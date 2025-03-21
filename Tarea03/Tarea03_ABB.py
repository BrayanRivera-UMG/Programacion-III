import csv
import os
import graphviz

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
        self.visualizacion_pendiente = False
    
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
        self.visualizacion_pendiente = True
        
    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
    
    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        return self._buscar_recursivo(nodo.derecha, valor)
    
    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)
        self.visualizacion_pendiente = True
        
    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return None
        
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None and nodo.derecha is None:
                return None
            
            if nodo.izquierda is None:
                return nodo.derecha
            if nodo.derecha is None:
                return nodo.izquierda
            
            sucesor = self._encontrar_minimo(nodo.derecha)
            nodo.valor = sucesor.valor
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, sucesor.valor)
        
        return nodo
    
    def _encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual
    
    def borrar_arbol(self):
        self.raiz = None
        self.visualizacion_pendiente = True
        return True

    def cargar_desde_csv(self, ruta_archivo):
        try:
            with open(ruta_archivo, 'r') as archivo:
                lector_csv = csv.reader(archivo)
                for fila in lector_csv:
                    for valor in fila:
                        try:
                            self.insertar(int(valor.strip()))
                        except ValueError:
                            print(f"Advertencia: No se pudo convertir '{valor}' a entero. Se omitirá.")
            print(f"Datos cargados exitosamente desde {ruta_archivo}")
            return True
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_archivo}")
            return False
        except Exception as e:
            print(f"Error al cargar el archivo: {str(e)}")
            return False
    
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
    
    def mostrar_visualizacion(self):
        if not self.visualizacion_pendiente:
            print("No hay cambios pendientes en el árbol para visualizar.")
            return
        
        dot = self.generar_visualizacion()
        if dot is None:
            print("El árbol está vacío, no hay nada que visualizar.")
            return
            
        try:
            dot.view()
            self.visualizacion_pendiente = False
            print("Visualización del árbol generada correctamente.")
        except Exception as e:
            print(f"Error al generar la visualización: {str(e)}")
    
    def convertir_a_binario(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado
    
    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.derecha, resultado)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    arbol = ArbolBinarioBusqueda()
    
    while True:
        print("\n *** MENU PRINCIPAL *** ")
        print("=== ÁRBOL BINARIO DE BÚSQUEDA ===")
        print("1. Insertar valor")
        print("2. Buscar valor")
        print("3. Eliminar valor")
        print("4. Cargar desde archivo CSV")
        print("5. Convertir a binario")
        print("6. Mostrar árbol")
        print("7. Borrar Todo el Arbol (s/n)")
        print("8. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        limpiar_pantalla()
        if opcion == "1":
            try:
                valor = int(input("Ingrese el valor a insertar: "))
                arbol.insertar(valor)
                print(f"Valor {valor} insertado correctamente.")
            except ValueError:
                print("Error: Debe ingresar un número entero.")
        
        elif opcion == "2":
            try:
                valor = int(input("Ingrese el valor a buscar: "))
                if arbol.buscar(valor):
                    print(f"El valor {valor} se encuentra en el árbol.")
                else:
                    print(f"El valor {valor} no se encuentra en el árbol.")
            except ValueError:
                print("Error: Debe ingresar un número entero.")
        
        elif opcion == "3":
            try:
                valor = int(input("Ingrese el valor a eliminar: "))
                if arbol.buscar(valor):
                    arbol.eliminar(valor)
                    print(f"Valor {valor} eliminado correctamente.")
                else:
                    print(f"El valor {valor} no se encuentra en el árbol.")
            except ValueError:
                print("Error: Debe ingresar un número entero.")
        
        elif opcion == "4":
            ruta_archivo = input("Ingrese la ruta del archivo CSV: ")
            arbol.cargar_desde_csv(ruta_archivo)
        
        elif opcion == "5":
            resultado = arbol.convertir_a_binario()
            print("Representación binaria (inorden):", resultado)
        
        elif opcion == "6":
            arbol.mostrar_visualizacion()
        
        elif opcion == "7":
            confirmacion = input("¿Está seguro de que desea borrar todo el árbol? (s/n): ")
            if confirmacion.lower() == 's':
                arbol.borrar_arbol()
                print("El árbol ha sido borrado completamente.")
            else:
                print("Operación cancelada.")

        elif opcion == "8":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

        input("\n Presione ENTER para volver al Menu Principal...")

if __name__ == "__main__":
    menu_principal()
