import pytest
from Ejercicio6 import lista_precios


def test_lista_precios_descuento_basico():
    """
    Verifica que el descuento del 10% se aplique correctamente.
    """
    productos = [
        {"nombre": "camisa", "precio": 50000},
        {"nombre": "pantalon", "precio": 120000},
        {"nombre": "chaqueta", "precio": 80000},
    ]
    resultado = lista_precios(productos)
    assert resultado[0]["precio"] == 45000.00
    assert resultado[1]["precio"] == 108000.00
    assert resultado[2]["precio"] == 72000.00


def test_lista_precios_tipo_datos():
    """
    Verifica que se devuelva una lista de diccionarios con las claves correctas.
    """
    productos = [{"nombre": "zapatos", "precio": 100000}]
    resultado = lista_precios(productos)
    assert isinstance(resultado, list)
    assert isinstance(resultado[0], dict)
    assert set(resultado[0].keys()) == {"nombre", "precio"}


def test_lista_precios_redondeo():
    """
    Verifica que los precios estén redondeados correctamente a dos decimales.
    """
    productos = [{"nombre": "gafas", "precio": 99999.999}]
    resultado = lista_precios(productos)
    assert resultado[0]["precio"] == round(99999.999 * 0.9, 2)
