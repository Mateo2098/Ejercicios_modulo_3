from functools import reduce
from rich.console import Console
from rich.table import Table


def suma_total(numeros: list[int]) -> int:
    """
    Calcula la suma total de una lista de números usando reduce.
    """
    return reduce(lambda x, y: x + y, numeros)


def concatenar_texto(palabras: list[str]) -> str:
    """
    Concatena una lista de strings usando reduce.
    """
    return reduce(lambda x, y: x + y, palabras)


def mostrar_tabla(resultados: dict[str, str]):
    """
    Muestra los resultados en una tabla usando Rich.
    """
    console = Console()
    tabla = Table(title=" Resultados con reduce()", header_style="bold magenta")

    tabla.add_column("Operación", style="cyan", justify="center")
    tabla.add_column("Resultado", style="green", justify="center")

    for clave, valor in resultados.items():
        tabla.add_row(clave, str(valor))

    console.print(tabla)


def main():
    numeros = [1, 2, 3, 4, 5]
    palabras = ["Hola", " ", "SENA", "!"]

    total = suma_total(numeros)
    frase = concatenar_texto(palabras)

    resultados = {
        "Suma Total": total,
        "Frase Concatenada": frase
    }

    mostrar_tabla(resultados)


if __name__ == "__main__":
    main()
