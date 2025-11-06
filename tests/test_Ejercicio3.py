import pytest
from rich.console import Console
from Ejercicio3 import crear_contador, limite_conteo, mostrar_contadores

def test_crear_contador_incrementa():
    """
    Verifica que el contador se incremente correctamente en cada llamada.
    """
    contador = crear_contador()
    assert contador() == 1
    assert contador() == 2
    assert contador() == 3


def test_contadores_independientes():
    """
    Verifica que los contadores sean independientes entre sí.
    """
    contador_a = crear_contador()
    contador_b = crear_contador()

    assert contador_a() == 1
    assert contador_a() == 2
    assert contador_b() == 1


def test_limite_conteo():
    """
    Verifica que la función limite_conteo funcione correctamente.
    """
    assert not limite_conteo(3, limite=4)
    assert limite_conteo(4, limite=4)
    assert not limite_conteo(5, limite=4)  # pasa del límite, ya no es igual


def test_mostrar_contadores(capsys):
    """
    Verifica que mostrar_contadores imprima correctamente usando Rich.
    """
    resultados = {"Contador 1": [1, 2, 3, 4]}
    mostrar_contadores(resultados)
    salida = capsys.readouterr().out

    assert "Resultados de Contadores" in salida
    assert "Contador 1" in salida
    assert "1, 2, 3, 4" in salida
