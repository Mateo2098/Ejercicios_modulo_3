from typing import Any
from rich.console import Console
from rich.table import Table


def lista_precios(productos: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Aplica un 10% de descuento a la lista de productos.
    """
    precios_desc = list(
        map(lambda p: {"nombre": p["nombre"], "precio": round(p["precio"] * 0.9, 2)}, productos)
    )
    return precios_desc


def mostrar_tabla(productos: list[dict[str, Any]]) -> None:
    """
    Muestra los productos con su descuento usando Rich.
    """
    console = Console()
    tabla = Table(title=" Lista con 10% de descuento ", header_style="bold magenta")

    tabla.add_column("Producto", style="cyan", justify="center")
    tabla.add_column("Precio con Descuento", style="green", justify="center")

    for p in productos:
        tabla.add_row(p["nombre"], f"${p['precio']:.2f}")

    console.print(tabla)


def main() -> None:
    productos = [
        {"nombre": "camisa", "precio": 50000},
        {"nombre": "pantalon", "precio": 120000},
        {"nombre": "chaqueta", "precio": 80000},
    ]

    productos_desc = lista_precios(productos)
    mostrar_tabla(productos_desc)


if __name__ == "__main__":
    main()
