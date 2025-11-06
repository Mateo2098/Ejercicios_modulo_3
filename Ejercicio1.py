from rich.table import Table
from rich.console import Console


def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso (float): Peso de la persona en kilogramos.
        altura (float): Altura de la persona en metros.

    Returns:
        float: Valor del IMC calculado.
    """
    if altura <= 0:
        raise ValueError("La estatura debe ser mayor a 0")

    imc = peso / (altura**2)
    return imc


def interpretar_imc(imc: float) -> str:
    """
    Interpreta el resultado del IMC y devuelve una categoría descriptiva.

    Args:
        imc (float): Índice de Masa Corporal calculado.

    Returns:
        str: Categoría del IMC.
    """
    if imc < 18.5:
        return f"Su IMC es {round(imc, 2)}: Destrunido y re flaco."
    elif 18.5 <= imc < 25:
        return f"Su IMC es {round(imc, 2)}: usted esta una re chimba."
    elif 25 <= imc < 30:
        return f"Su IMC es {round(imc, 2)}: ojo con eso baje de peso."
    else:
        return (
            f"Su IMC es {round(imc, 2)}: no le llama la atension un gym o una cirugia?."
        )


def tabla_resultado(peso: float, altura: float, imc: float) -> None:
    """
    Muestra los resultados

    Args:
        peso (float): Peso de la persona en kilogramos
        estatura (float): Estatura de la persona en metros
        imc (float): Valor del IMC calculado
        categoria (str): Categoria del resultado
    """

    console = Console()

    table = Table(title="Resultado del IMC")

    table.add_column("Dato", style="bold cyan", justify="center")
    table.add_column("valor", style="bold yellow", justify="center")

    table.add_row("Peso (Kg)", f"{peso:.2f}")
    table.add_row("Estatura (M)", f"{altura:.2f}")
    table.add_row("IMC", f"{imc:.2f}")

    console.print(table)


def main():
    """
    Función principal que orquesta el programa.
    Solicita los datos del usuario, calcula el IMC e imprime la interpretación.

    Arg:
    peso (float): Peso de la persona en kilogramos.
    altura (float): Altura de la persona en metros.

    Returns:
    """
    peso = float(input("Digite su peso en kilogramos: "))
    altura = float(input("Digite su altura en metros: "))

    imc = calcular_imc(peso, altura)
    resultado = interpretar_imc(imc)
    print(resultado)


if __name__ == "__main__":
    main()
