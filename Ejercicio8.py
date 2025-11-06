from rich.console import Console
from rich.table import Table


def palabras_mayus_largas(texto: str):
    """
    Retorna una lista de palabras en MAYÚSCULAS con más de 5 letras.
    """
    palabras = texto.split()
    lista_mayus = [palabra.upper() for palabra in palabras if len(palabra) > 5]
    return lista_mayus


def longitudes_palabras(lista_palabras: list[str]):
    """
    Retorna un diccionario con las palabras y su longitud.
    """
    diccionario = {palabra: len(palabra) for palabra in lista_palabras}
    return diccionario


def mostrar_tabla(diccionario: dict[str, int]):
    """
    Muestra las palabras y sus longitudes en una tabla Rich.
    """
    console = Console()
    tabla = Table(title="📘 Palabras Mayúsculas con más de 5 letras 📘", header_style="bold blue")

    tabla.add_column("Palabra", style="cyan", justify="center")
    tabla.add_column("Longitud", style="green", justify="center")

    for palabra, longitud in diccionario.items():
        tabla.add_row(palabra, str(longitud))

    console.print(tabla)


def main():
    texto = (
        "Python es un lenguaje de PROGRAMACIÓN poderoso y versátil, "
        "utilizado en DESARROLLO web, CIENCIA de datos, y AUTOMATIZACIÓN."
    )

    lista_resultante = palabras_mayus_largas(texto)
    diccionario_resultante = longitudes_palabras(lista_resultante)

    if lista_resultante:
        mostrar_tabla(diccionario_resultante)
    else:
        print("No se encontraron palabras con más de 5 letras.")


if __name__ == "__main__":
    main()
