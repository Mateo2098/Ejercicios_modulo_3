import pytest
from Ejercicio8 import palabras_mayus_largas, longitudes_palabras

def test_palabras_mayus_largas():
    texto = "Hola esto es una PRUEBA de FUNCIONALIDAD del SISTEMA"
    resultado = palabras_mayus_largas(texto)
    assert "PRUEBA" in resultado
    assert "FUNCIONALIDAD" in resultado
    assert "SISTEMA" in resultado
    assert all(palabra.isupper() for palabra in resultado)
    assert all(len(palabra) > 5 for palabra in resultado)


def test_longitudes_palabras():
    lista = ["PRUEBA", "FUNCIONALIDAD"]
    resultado = longitudes_palabras(lista)
    assert resultado == {"PRUEBA": 6, "FUNCIONALIDAD": 14}


def test_lista_vacia():
    texto = "hola soy io"
    resultado = palabras_mayus_largas(texto)
    assert resultado == []
