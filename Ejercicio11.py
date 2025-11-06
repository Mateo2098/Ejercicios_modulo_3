from rich.console import Console
from rich.table import Table
import os

ARCHIVO_TAREAS = "tareas.txt"
console = Console()

def agregar_tarea(tarea: str):
    """Agrega una tarea al archivo de texto."""
    with open(ARCHIVO_TAREAS, "a", encoding="utf-8") as archivo:
        archivo.write(tarea + "\n")
    console.print(f"[green]Tarea agregada correctamente:[/green] {tarea}")

def ver_tareas() -> list[str]:
    """Lee todas las tareas guardadas en el archivo y las devuelve como lista."""
    if not os.path.exists(ARCHIVO_TAREAS):
        console.print(" [yellow]El archivo no existe todavía, creando uno nuevo...[/yellow]")
        open(ARCHIVO_TAREAS, "w").close()
        return []

    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        tareas = [linea.strip() for linea in archivo.readlines() if linea.strip()]
    return tareas

def mostrar_tareas():
    """Muestra las tareas en una tabla con Rich."""
    tareas = ver_tareas()
    tabla = Table(title="Lista de Tareas", header_style="bold blue")
    tabla.add_column("N°", justify="center", style="cyan")
    tabla.add_column("Tarea", justify="left", style="green")

    if not tareas:
        tabla.add_row("-", "No hay tareas por ahora... ")
    else:
        for i, tarea in enumerate(tareas, start=1):
            tabla.add_row(str(i), tarea)

    console.print(tabla)

def main():
    while True:
        console.print("\n[bold yellow]--- MENÚ GESTOR DE TAREAS ---[/bold yellow]")
        console.print("1 Agregar tarea")
        console.print("2 Ver tareas")
        console.print("3 Salir")

        opcion = input("\n Elige una opción (1-3): ").strip()

        if opcion == "1":
            tarea = input(" Escribe la nueva tarea: ").strip()
            if tarea == "":
                console.print("[red]No puedes agregar una tarea vacía, cerebro de mosquito![/red]")
            else:
                agregar_tarea(tarea)

        elif opcion == "2":
            mostrar_tareas()

        elif opcion == "3":
            console.print(" [bold green]Saliendo del gestor... Hasta la próxima![/bold green]")
            break
        else:
            console.print(" [red]Opción inválida, intenta otra vez![/red]")

if __name__ == "__main__":
    main()
