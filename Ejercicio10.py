from typing import Any
from rich.console import Console
from rich.table import Table


def explorar_estructura(elemento: Any, profundidad: int = 1, resultados: list[tuple] = None) -> list[tuple]:
    """
    Explora recursivamente cualquier estructura (listas, diccionarios, tuplas, etc.)
    y devuelve una lista con los valores no iterables junto con su profundidad.
    """
    if resultados is None:
        resultados = []

    if isinstance(elemento, dict):
        for clave, valor in elemento.items():
            explorar_estructura(valor, profundidad + 1, resultados)
    elif isinstance(elemento, (list, tuple, set)):
        for valor in elemento:
            explorar_estructura(valor, profundidad + 1, resultados)
    else:
        resultados.append((elemento, profundidad))

    return resultados


def mostrar_tabla(resultados: list[tuple]):
    """
    Muestra los valores y sus profundidades en una tabla con Rich.
    """
    console = Console()
    tabla = Table(title="Explorador de Estructuras Recursivo", header_style="bold blue")

    tabla.add_column("Valor", style="cyan", justify="center")
    tabla.add_column("Profundidad", style="green", justify="center")

    if resultados:
        for valor, profundidad in resultados:
            tabla.add_row(str(valor), str(profundidad))
    else:
        tabla.add_row("Nada que mostrar", "0")

    console.print(tabla)


def main():
    estructura = [1, [2, 3], {"a": 4, "b": [5, {"c": 6}]}]
    console = Console()
    console.print("[bold yellow]Explorando estructura compleja...[/bold yellow]")

    resultados = explorar_estructura(estructura)
    mostrar_tabla(resultados)


if __name__ == "__main__":
    main()
