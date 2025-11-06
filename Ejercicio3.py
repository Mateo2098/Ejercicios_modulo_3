from typing import Callable
from rich.console import Console
from rich.table import Table


def crear_contador() -> Callable[[], int]:
    """
    Crea un contador independiente que recuerda cuántas veces ha sido llamado.

    Returns:
        Callable[[], int]: Una función interna que incrementa y devuelve el conteo actual.
    """
    conteo = 0

    def incrementar() -> int:
        """
        Incrementa el valor del contador en 1 y lo devuelve.

        Returns:
            int: El número actual del contador después de incrementar.
        """
        nonlocal conteo
        conteo += 1
        return conteo

    return incrementar


def limite_conteo(valor: int, limite: int = 4) -> bool:
    """
    Verifica si el valor del contador ha alcanzado el límite especificado.

    Args:
        valor (int): Valor actual del contador.
        limite (int): Límite máximo permitido (por defecto 4).

    Returns:
        bool: True si se alcanzó el límite, False en caso contrario.
    """
    return valor == limite


def mostrar_contadores(resultados: dict[str, list[int]]) -> None:
    """
    Muestra los resultados de varios contadores en una tabla usando Rich.

    Args:
        resultados (dict[str, list[int]]): Diccionario donde las claves son los nombres
        de los contadores y los valores son listas con los resultados de las llamadas.
    """
    console = Console()

    tabla = Table(
        title="Resultados de Contadores",
        header_style="bold magenta",
        show_header=True,
    )

    tabla.add_column("Contador", style="cyan", justify="center")
    tabla.add_column("Llamadas Realizadas", style="white")

    for nombre, valores in resultados.items():
        valores_texto = ", ".join(map(str, valores))
        tabla.add_row(nombre, valores_texto)

    console.print(tabla)


def main():
    console = Console()
    contador1 = crear_contador()

    console.print("[bold green]Iniciando contador hasta el límite...[/bold green]\n")

    valores = []
    while True:
        valor_actual = contador1()
        valores.append(valor_actual)
        console.print(f"→ [cyan]El contador actual es:[/cyan] {valor_actual}")

        if limite_conteo(valor_actual, limite=4):
            console.print("[bold red]¡Límite alcanzado![/bold red]")
            break

    mostrar_contadores({"Contador 1": valores})


if __name__ == "__main__":
    main()
