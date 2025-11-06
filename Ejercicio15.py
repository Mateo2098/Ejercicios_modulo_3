from typing import Any, Dict, List
import json
import os
from rich.console import Console
from rich.table import Table

BIBLIOTECA_ARCHIVO = "biblioteca.json"
console = Console()


def cargar_biblioteca(ruta: str = BIBLIOTECA_ARCHIVO) -> List[Dict[str, Any]]:
    """
    Carga el estado de la biblioteca desde un archivo JSON.

    Args:
        ruta (str): Ruta del archivo JSON.

    Returns:
        List[Dict[str, Any]]: Lista de libros (cada libro es un diccionario).
    """
    if not os.path.exists(ruta):
        # Si no existe, creamos un archivo vacío con lista vacía
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        return []

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Si el archivo está corrupto, lo reiniciamos
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        return []


def guardar_biblioteca(
    libros: List[Dict[str, Any]], ruta: str = BIBLIOTECA_ARCHIVO
) -> None:
    """
    Guarda la lista de libros en el archivo JSON.

    Args:
        libros (List[Dict[str, Any]]): Lista de libros a guardar.
        ruta (str): Ruta del archivo JSON.
    """
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(libros, f, ensure_ascii=False, indent=4)


def prestar_libro(
    libros: List[Dict[str, Any]], libro_id: str, nombre_aprendiz: str
) -> bool:
    """
    Marca un libro como prestado a un aprendiz si está disponible.

    Args:
        libros (List[Dict[str, Any]]): Lista de libros.
        libro_id (str): ID del libro a prestar.
        nombre_aprendiz (str): Nombre del aprendiz.

    Returns:
        bool: True si la operación fue exitosa, False si no (no existe o ya prestado).
    """
    for libro in libros:
        if libro.get("libro_id") == libro_id:
            if libro.get("prestado_a"):
                # Ya está prestado
                return False
            libro["prestado_a"] = nombre_aprendiz
            return True
    return False  # No encontrado


def devolver_libro(libros: List[Dict[str, Any]], libro_id: str) -> bool:
    """
    Marca un libro como disponible (prestado_a = None).

    Args:
        libros (List[Dict[str, Any]]): Lista de libros.
        libro_id (str): ID del libro a devolver.

    Returns:
        bool: True si se devolvió correctamente, False si no se encontró el libro.
    """
    for libro in libros:
        if libro.get("libro_id") == libro_id:
            libro["prestado_a"] = None
            return True
    return False


def buscar_libro(libros: List[Dict[str, Any]], query: str) -> List[Dict[str, Any]]:
    """
    Busca libros cuyo título contenga la query (case-insensitive).

    Args:
        libros (List[Dict[str, Any]]): Lista de libros.
        query (str): Texto a buscar en el título.

    Returns:
        List[Dict[str, Any]]: Lista de libros coincidentes.
    """
    q = query.strip().lower()
    return [l for l in libros if q in l.get("titulo", "").lower()]


def ver_libros_prestados(libros: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Devuelve la lista de libros que están prestados (prestado_a != None).

    Args:
        libros (List[Dict[str, Any]]): Lista de libros.

    Returns:
        List[Dict[str, Any]]: Libros prestados.
    """
    return [l for l in libros if l.get("prestado_a")]


def mostrar_libros(libros: List[Dict[str, Any]]) -> None:
    """
    Muestra una tabla con todos los libros y su estado.
    """
    table = Table(title=" Biblioteca - Inventario", header_style="bold magenta")
    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Título", justify="left", style="white")
    table.add_column("Prestado a", justify="left", style="green")

    if not libros:
        console.print("[bold yellow]No hay libros en la biblioteca.[/bold yellow]")
        return

    for l in libros:
        table.add_row(
            str(l.get("libro_id", "")),
            l.get("titulo", ""),
            str(l.get("prestado_a") or "Disponible"),
        )

    console.print(table)


def mostrar_libros_prestados(libros: List[Dict[str, Any]]) -> None:
    """
    Muestra en consola los libros que están prestados (uso de rich).
    """
    prestados = ver_libros_prestados(libros)
    table = Table(title=" Libros Prestados", header_style="bold red")
    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Título", justify="left", style="white")
    table.add_column("Prestado a", justify="left", style="green")

    if not prestados:
        console.print("[bold yellow]No hay libros prestados ahora mismo.[/bold yellow]")
        return

    for l in prestados:
        table.add_row(
            str(l.get("libro_id", "")), l.get("titulo", ""), str(l.get("prestado_a"))
        )

    console.print(table)


def main() -> None:
    """
    Interfaz de consola minimal para interactuar con la biblioteca.
    """
    ruta = BIBLIOTECA_ARCHIVO
    libros = cargar_biblioteca(ruta)

    while True:
        console.print("\n[bold yellow]--- MENÚ BIBLIOTECA ---[/bold yellow]")
        console.print("1 Ver todos los libros")
        console.print("2 Ver libros prestados")
        console.print("3 Buscar libro por título")
        console.print("4 Prestar libro")
        console.print("5 Devolver libro")
        console.print("6 Salir")

        opcion = input("Elige una opción (1-6): ").strip()

        if opcion == "1":
            mostrar_libros(libros)
        elif opcion == "2":
            mostrar_libros_prestados(libros)
        elif opcion == "3":
            q = input("Ingresa texto para buscar en títulos: ").strip()
            encontrados = buscar_libro(libros, q)
            if encontrados:
                mostrar_libros(encontrados)
            else:
                console.print("[red]No se encontraron coincidencias.[/red]")
        elif opcion == "4":
            lid = input("ID del libro a prestar: ").strip()
            aprendiz = input("Nombre del aprendiz: ").strip()
            if prestar_libro(libros, lid, aprendiz):
                guardar_biblioteca(libros, ruta)
                console.print(f" Libro {lid} prestado a {aprendiz}.")
            else:
                console.print(
                    "[red]No se pudo prestar (no existe o ya está prestado).[/red]"
                )
        elif opcion == "5":
            lid = input("ID del libro a devolver: ").strip()
            if devolver_libro(libros, lid):
                guardar_biblioteca(libros, ruta)
                console.print(f" Libro {lid} devuelto y disponible.")
            else:
                console.print("[red]No se encontró el libro indicado.[/red]")
        elif opcion == "6":
            console.print("[bold green]Saliendo... ¡nos vidrios![/bold green]")
            break
        else:
            console.print("[red]Opción inválida, inténtalo de nuevo.[/red]")


if __name__ == "__main__":
    main()
