import csv
import json
from rich.table import Table
from rich.console import Console
from rich.panel import Panel


def leer_csv(nombre_archivo: str) -> list[dict]:
    """
    Lee un archivo CSV y devuelve una lista de diccionarios con los datos.
    """
    with open(nombre_archivo, "r", encoding="utf-8") as file:
        lector = csv.DictReader(file)
        return list(lector)


def leer_json(nombre_archivo: str) -> list[dict]:
    """
    Lee un archivo JSON y devuelve la lista de datos.
    """
    with open(nombre_archivo, "r", encoding="utf-8") as file:
        return json.load(file)


def generar_reporte(estudiantes: list[dict], cursos: list[dict], archivo_salida: str) -> None:
    """
    Combina la información de estudiantes y cursos, genera un reporte en texto
    y lo muestra en consola con Rich antes de guardarlo.
    """
    console = Console()
    reporte = []

    for estudiante in estudiantes:
        cursos_tomados = [
            c["nombre_curso"] for c in cursos if c["id_estudiante"] == estudiante["id"]
        ]
        reporte.append({"nombre": estudiante["nombre"], "cursos": cursos_tomados})

    table = Table(title=" Reporte de Estudiantes y Cursos", header_style="bold green")
    table.add_column("Estudiante", style="cyan", justify="left")
    table.add_column("Cursos Tomados", style="white", justify="left")

    for r in reporte:
        cursos_texto = ", ".join(r["cursos"]) if r["cursos"] else "Sin cursos"
        table.add_row(r["nombre"], cursos_texto)

    console.print(Panel.fit(" Vista previa del reporte antes de guardar:", style="bold blue"))
    console.print(table)


    with open(archivo_salida, "w", encoding="utf-8") as file:
        for r in reporte:
            file.write(f"{r['nombre']}: {', '.join(r['cursos']) or 'Sin cursos'}\n")

    console.print(Panel.fit(f"Reporte guardado en: {archivo_salida}", style="bold green"))


def main():
    estudiantes = leer_csv("estudiantes.csv")
    cursos = leer_json("cursos.json")
    generar_reporte(estudiantes, cursos, "reporte.txt")


if __name__ == "__main__":
    main()
