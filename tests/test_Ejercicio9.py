import pytest
from Ejercicio9 import suma_total, concatenar_texto

def test_suma_total():
    numeros = [1, 2, 3, 4, 5]
    assert suma_total(numeros) == 15

def test_concatenar_texto():
    palabras = ["Hola", " ", "SENA", "!"]
    assert concatenar_texto(palabras) == "Hola SENA!"

def test_lista_vacia_suma():
    with pytest.raises(TypeError):
        suma_total([])

def test_lista_vacia_concatenar():
    with pytest.raises(TypeError):
        concatenar_texto([])
