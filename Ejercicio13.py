import json
from rich.console import Console
from rich.table import Table
from typing import List, Dict

ARCHIVO = "inventario.json"


def cargar_inventario() -> List[Dict]:
    """
    Carga el inventario desde el archivo JSON. Si no existe, crea uno vacío.
    """
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("No se encontró el archivo, creando uno nuevo ")
        return []
    except json.JSONDecodeError:
        print("El archivo JSON está vacío o dañado, creando uno nuevo ")
        return []


def guardar_inventario(inventario: List[Dict]) -> None:
    """
    Guarda la lista de inventario en el archivo JSON.
    """
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(inventario, f, indent=4, ensure_ascii=False)


def agregar_producto(inventario: List[Dict]) -> None:
    """
    Agrega un nuevo producto al inventario.
    """
    nombre = input("Nombre del producto: ").strip()
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    guardar_inventario(inventario)
    print(f" Producto '{nombre}' agregado correctamente.")


def vender_producto(inventario: List[Dict]) -> None:
    """
    Resta cantidad al producto vendido.
    """
    nombre = input("Nombre del producto vendido: ").strip()
    cantidad_vendida = int(input("Cantidad vendida: "))

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            if producto["cantidad"] >= cantidad_vendida:
                producto["cantidad"] -= cantidad_vendida
                guardar_inventario(inventario)
                print(f" Venta realizada: {cantidad_vendida} unidades de '{nombre}'.")
            else:
                print(" No hay suficiente cantidad en inventario.")
            return

    print(" Producto no encontrado en el inventario.")


def mostrar_inventario(inventario: List[Dict]) -> None:
    """
    Muestra el inventario en una tabla usando rich.
    """
    console = Console()
    tabla = Table(title=" Inventario Actual", header_style="bold magenta")
    tabla.add_column("Nombre", style="cyan", justify="center")
    tabla.add_column("Precio", justify="center")
    tabla.add_column("Cantidad", justify="center")

    if not inventario:
        console.print("[bold red]No hay productos en el inventario.[/bold red]")
        return

    for p in inventario:
        tabla.add_row(p["nombre"], f"${p['precio']:.2f}", str(p["cantidad"]))

    console.print(tabla)


def main():
    inventario = cargar_inventario()

    while True:
        print("\n MENÚ DE INVENTARIO ")
        print("1. Ver inventario")
        print("2. Agregar producto")
        print("3. Vender producto")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            agregar_producto(inventario)
        elif opcion == "3":
            vender_producto(inventario)
        elif opcion == "4":
            print(" Cerrando el gestor... nos vidrios.")
            break
        else:
            print(" Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
