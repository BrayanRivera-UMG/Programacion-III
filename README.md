# Tarea01

# 1. Definición de la Clase Nodo
Cada nodo almacena un nombre, apellido y carnet. También tiene punteros siguiente y anterior.

```
class Nodo {
    constructor(nombre, apellido, carnet) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.carnet = carnet;
        this.siguiente = null;
        this.anterior = null;
    }
}
```


## 2. Clase ListaDoblementeEnlazada
Esta clase maneja la lista doblemente enlazada.

## 2.1. Insertar al principio
Si la lista está vacía, el nuevo nodo se convierte en cabeza y cola. Si no, el nodo nuevo se enlaza al inicio.
```
insertar_al_principio(nombre, apellido, carnet) {
    let nuevo_nodo = new Nodo(nombre, apellido, carnet);
    if (!this.cabeza) {
        this.cabeza = this.cola = nuevo_nodo;
    } else {
        nuevo_nodo.siguiente = this.cabeza;
        this.cabeza.anterior = nuevo_nodo;
        this.cabeza = nuevo_nodo;
    }
}
```
## 2.2. Insertar al final
Si la lista está vacía, se asigna el nodo como cabeza y cola. De lo contrario, se enlaza al final.
```
insertar_al_final(nombre, apellido, carnet) {
    let nuevo_nodo = new Nodo(nombre, apellido, carnet);
    if (!this.cola) {
        this.cabeza = this.cola = nuevo_nodo;
    } else {
        nuevo_nodo.anterior = this.cola;
        this.cola.siguiente = nuevo_nodo;
        this.cola = nuevo_nodo;
    }
}
```
## 2.3. Eliminar por valor (carnet)
Busca el nodo con el carnet especificado y lo elimina ajustando los punteros.
```
eliminar_por_valor(carnet) {
    let actual = this.cabeza;
    while (actual) {
        if (actual.carnet === carnet) {
            if (actual.anterior) {
                actual.anterior.siguiente = actual.siguiente;
            } else {
                this.cabeza = actual.siguiente;
            }
            if (actual.siguiente) {
                actual.siguiente.anterior = actual.anterior;
            } else {
                this.cola = actual.anterior;
            }
            console.log("Nodo eliminado.");
            return;
        }
        actual = actual.siguiente;
    }
    console.log("Nodo no encontrado.");
}
```
## 3. Menú de Opciones
El usuario interactúa con la lista a través de un menú
```
menu() {
    let lista = new ListaDoblementeEnlazada();
    while (true) {
        console.log("\nMenú de opciones:");
        console.log("1. Insertar al principio");
        console.log("2. Insertar al final");
        console.log("3. Eliminar por carnet");
        console.log("4. Mostrar lista");
        console.log("5. Imprimir gráfico");
        console.log("6. Salir");
        let opcion = prompt("Seleccione una opción: ");
        if (opcion === "1") {
            let nombre = prompt("Ingrese el nombre: ");
            let apellido = prompt("Ingrese el apellido: ");
            let carnet = prompt("Ingrese el carnet: ");
            lista.insertar_al_principio(nombre, apellido, carnet);
        } else if (opcion === "2") {
            let nombre = prompt("Ingrese el nombre: ");
            let apellido = prompt("Ingrese el apellido: ");
            let carnet = prompt("Ingrese el carnet: ");
            lista.insertar_al_final(nombre, apellido, carnet);
        } else if (opcion === "3") {
            let carnet = prompt("Ingrese el carnet a eliminar: ");
            lista.eliminar_por_valor(carnet);
        } else if (opcion === "4") {
            lista.mostrar_lista();
        } else if (opcion === "5") {
            lista.generar_grafico();
        } else if (opcion === "6") {
            console.log("Saliendo del programa...");
            break;
        } else {
            console.log("Opción inválida, intente de nuevo.");
        }
    }
}
```
