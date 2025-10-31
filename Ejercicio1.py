def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso (float): Peso de la persona en kilogramos.
        altura (float): Altura de la persona en metros.

    Returns:
        float: Valor del IMC calculado.
    """
    return peso / (altura**2)


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
