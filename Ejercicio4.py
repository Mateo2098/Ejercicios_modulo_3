from typing import Callable
import re
from rich.table import Table
from rich.console import Console


def aplicar_validador(datos, validador):
    """
    Aplica un validador a una lista de datos y devuelve solo los válidos.
    """
    return [dato for dato in datos if validador(dato)]


def email_validado(email: str) -> bool:
    """
    Valida que el correo contenga '@' y '.'.
    """
    return "@" in email and "." in email


def numero_valido(numero: str) -> bool:
    """
    Verifica que el número sea mayor a 10.
    """
    try:
        return int(numero) > 10
    except ValueError:
        return False


def mostrar_tabla(titulo: str, datos: list[str]):
    """
    Muestra los datos validados en una tabla usando Rich.
    """
    console = Console()
    table = Table(title=titulo, header_style="bold green")

    table.add_column("Dato", justify="center", style="cyan")

    if datos:
        for d in datos:
            table.add_row(d)
    else:
        table.add_row("No hay datos válidos")

    console.print(table)


def main():
    emails = ["andres_69@erome.com", "vergudo_en_4@erome.com", "andresfelipe.com"]
    numeros = ["15", "10", "03", "69", "0", "9"]

    email_validos = aplicar_validador(emails, email_validado)
    print("Emails validados:", email_validos)

    numero_validos = aplicar_validador(numeros, numero_valido)
    print("Números válidos:", numero_validos)

    # Visualización opcional con Rich
    mostrar_tabla("Emails válidos", email_validos)
    mostrar_tabla("Números válidos", numero_validos)


if __name__ == "__main__":
    main()
