import csv
from rich.console import Console
from rich.table import Table

console = Console()


def analizar_csv(nombre_archivo: str, columna: str) -> dict:
    """
    Analiza un archivo CSV y calcula el promedio, máximo y mínimo
    de la columna numérica especificada.

    Args:
        nombre_archivo (str): Ruta del archivo CSV.
        columna (str): Nombre de la columna numérica.

    Returns:
        dict: Diccionario con promedio, máximo y mínimo.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            valores = []
            for fila in lector:
                try:
                    valor = float(fila[columna])
                    valores.append(valor)
                except ValueError:
                    console.print(
                        f"[yellow]Valor no numérico ignorado:[/yellow] {fila[columna]}"
                    )

            if not valores:
                console.print(
                    f"[red]No se encontraron valores válidos en la columna '{columna}'[/red]"
                )
                return {}

            promedio = sum(valores) / len(valores)
            maximo = max(valores)
            minimo = min(valores)

            resultados = {
                "Promedio": round(promedio, 2),
                "Máximo": maximo,
                "Mínimo": minimo,
            }

            return resultados

    except FileNotFoundError:
        console.print(
            f" [red]El archivo '{nombre_archivo}' no existe... verifica el nombre![/red]"
        )
        return {}
    except KeyError:
        console.print(f"[red]La columna '{columna}' no existe en el archivo![/red]")
        return {}


def mostrar_resultados(resultados: dict):
    """Muestra los resultados del análisis en una tabla con rich."""
    if not resultados:
        console.print("[yellow]No hay resultados para mostrar...[/yellow]")
        return

    tabla = Table(title=" Análisis de Datos CSV", header_style="bold blue")
    tabla.add_column("Medida", justify="center", style="cyan")
    tabla.add_column("Valor", justify="center", style="green")

    for clave, valor in resultados.items():
        tabla.add_row(clave, str(valor))

    console.print(tabla)


def main():
    console.print("[bold yellow]=== ANALIZADOR DE DATOS CSV ===[/bold yellow]")
    nombre_archivo = input(" Ingresa el nombre del archivo CSV: ").strip()
    columna = input("Ingresa el nombre de la columna numérica: ").strip()

    resultados = analizar_csv(nombre_archivo, columna)
    mostrar_resultados(resultados)


if __name__ == "__main__":
    main()
