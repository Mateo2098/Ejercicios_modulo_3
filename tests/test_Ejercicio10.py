import pytest
from Ejercicio10 import explorar_estructura

def test_lista_simple():
    datos = [1, 2, 3]
    resultado = explorar_estructura(datos)
    assert (1, 2) in resultado
    assert (2, 2) in resultado
    assert (3, 2) in resultado

def test_diccionario_anidado():
    datos = {"a": {"b": {"c": 5}}}
    resultado = explorar_estructura(datos)
    assert (5, 3) in resultado

def test_estructura_mixta():
    datos = [1, [2, {"x": 3}]]
    resultado = explorar_estructura(datos)
    assert (1, 1) in resultado or (1, 2) in resultado
    assert (2, 2) in resultado or (2, 3) in resultado
    assert (3, 3) in resultado or (3, 4) in resultado

def test_vacio():
    datos = []
    resultado = explorar_estructura(datos)
    assert resultado == []
