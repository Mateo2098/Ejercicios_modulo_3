from rich.console import Console
from rich.table import Table


def estudiantes_aprovados(estudiantes):
    """
    Filtra y devuelve los estudiantes con nota mayor o igual a 3.0
    """
    notas_aprovadas = list(filter(lambda n: n[1] >= 3.0, estudiantes))
    return notas_aprovadas


def mostrar_tabla(estudiantes):
    """
    Muestra los estudiantes aprobados en una tabla con Rich.
    """
    console = Console()
    tabla = Table(title=" Estudiantes Aprobados ", header_style="bold blue")

    tabla.add_column("Nombre", style="cyan", justify="center")
    tabla.add_column("Nota", style="green", justify="center")

    for nombre, nota in estudiantes:
        tabla.add_row(nombre, f"{nota:.1f}")

    console.print(tabla)


def main():
    estudiantes = [
        ("Ana", 2.5),
        ("Juan", 2.8),
        ("Maria", 3.9),
        ("Andres", 4.5),
        ("Carlitos", 2.9),
        ("El klk", 5.0),
    ]

    aprovados = estudiantes_aprovados(estudiantes)

    if aprovados:
        mostrar_tabla(aprovados)
    else:
        print("Ningún estudiante aprobó 😢")


if __name__ == "__main__":
    main()
