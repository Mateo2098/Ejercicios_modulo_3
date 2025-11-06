from typing import NoReturn
from rich.table import Table
from rich.console import Console

TASA_IVA = 0.19


def calculo_iva(precio_base: float):
    """
    Calcula el valor del IVA y el total con IVA aplicado.
    """
    valor1 = precio_base * TASA_IVA
    valor2 = precio_base + valor1  # ✅ se corrige: sumar IVA, no restar
    return valor1, valor2


def actualizar_tasa(nueva_tasa: float) -> None:
    """
    Actualiza la tasa global de IVA.
    """
    global TASA_IVA
    TASA_IVA = nueva_tasa


def main() -> NoReturn:
    """
    Función principal que solicita datos al usuario y muestra cálculos del IVA.
    """
    while True:
        try:
            precio_base = float(input("Ingresa el valor actual: "))
            if precio_base < 0:
                print("Como va a ser un valor negativo te falla el ..🧠🧠")
            else:
                break
        except ValueError:
            print("Como va a ser un precio sin ningun valor, IDIOTA")

    valor1, valor2 = calculo_iva(precio_base)
    print(f"El precio del valor de iva es: {valor1:.2f}")
    print(f"El valor total con iva es: {valor2:.2f}")

    while True:
        try:
            nueva_tasa = float(input("Ingresa el valor de tasa actual: "))
            if nueva_tasa < 0:
                print("De nuevo?... estas mal del 🥥🥥")
            else:
                actualizar_tasa(nueva_tasa)
                break
        except ValueError:
            print("No puedo creer lo pendejo, digita un valor REAL")

    valor3, valor4 = calculo_iva(precio_base)
    print("Calculo con la nueva tasa")
    print(f"El precio del valor de iva es: {valor3:.2f}")
    print(f"El valor total con iva es: {valor4:.2f}")


if __name__ == "__main__":
    main()
