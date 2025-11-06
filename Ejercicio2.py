from typing import  Dict
from rich.console import Console
from rich.table import Table


def crear_perfil(nombre: str, edad: int, *hobbies: list[str], **redes: str)-> str:
    """
    Esta funcion muestra un perfil con nombre, edad, hobbies y redes
    Arg:

    return:
        perfil(str): perfil con nombre, edad, hobbies, redes
    """

    table = Table(
        title=f"Perfil de {nombre}",
        show_header=True,  # encabezado
        header_style="bold green"  # Color
    )

    # columnas principales
    table.add_column("Campo", justify="left", style="cyan", no_wrap=True)
    table.add_column("Información", style="white")

    # Información básica
    table.add_row("Nombre", nombre)
    table.add_row("Edad", str(edad))
    table.add_row("Hobbies", ", ".join(hobbies) if hobbies else "No especificados")

    if redes:
        redes = "\n".join(f"{red}:{usuario}" for red, usuario in redes.items())
        table.add_row("Redes Sociales", redes)

    else:
        table.add_row("Redes Sociales", "No registradas")

    console = Console()
    console.print(table)

    perfil_texto = (
        f"Perfil de {nombre}\n"
        f"Edad: {edad}\n"
        f"Hobbies:{', '.join(hobbies) if hobbies else "No especificados"}\n"
        f"Redes:{', '.join(redes.keys()) if redes else "No registradas"}"
    )

    return perfil_texto


def main()-> tuple:
    """
    Esta funcion ingresa los datos para la creacion del perfil
    Arg:
        nombre (str): nombre del perfil
        edad (int): edad del perfil
        hobbies (str): hobbies del perfil
        redes (str): redes del perfil
    :return:
    """
    while True:
        nombre = str(input("Ingresa el nombre del usuario: ")).strip()
        if nombre == " " or nombre is None:
            print("el campo tiene que etar lleno baboso")
        else:
            break
    while True:
        try:
            edad = int(input("Edad: "))
            if edad < 0:
                print("como va a estar una edad en negativo? te falla 🧠🧠🧠🧠?")
            elif edad > 110:
                print("Como va a tener mas de 110, usted es un mentiroso")
            else:
                break
        except ValueError:
            print("el campo tiene que etar lleno baboso")

    hobbies = input("Hobbies (separa por comas): ").split(",")
    hobbies = [h.strip() for h in hobbies if h.strip()]
    redes_input = input("Redes (formato: Instagram:@user, Facebook:user): ").split(",")
    redes = {}
    for r in redes_input:
        if ":" in r:
            red, usuario = r.split(":", 1)
            redes[red.strip()] = usuario.strip()

    perfil = crear_perfil(nombre, edad, hobbies, **redes)
    print(perfil)
    return nombre, edad, hobbies, redes


if __name__ == "__main__":
    console = Console()

    console.print("[bold green] Bienvenido al generador de Perfiles [/bold green]\n")

    nombre, edad, hobbies, redes = main()

    console.print("\n[bold yellow] Perfil Generado: [/bold yellow]\n")
    crear_perfil(nombre, edad, hobbies, **redes)

