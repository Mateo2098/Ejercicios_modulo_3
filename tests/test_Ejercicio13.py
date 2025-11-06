import json
import os
import pytest
from Ejercicio13 import (
    cargar_inventario,
    guardar_inventario,
    agregar_producto,
    vender_producto,
    mostrar_inventario,
    ARCHIVO,
)

@pytest.fixture(autouse=True)
def limpiar_archivo():
    """Crea un inventario limpio antes de cada prueba."""
    if os.path.exists(ARCHIVO):
        os.remove(ARCHIVO)
    yield
    if os.path.exists(ARCHIVO):
        os.remove(ARCHIVO)

def test_cargar_inventario_vacio():
    """Debe devolver lista vacía si no existe el archivo."""
    inventario = cargar_inventario()
    assert isinstance(inventario, list)
    assert inventario == []

def test_guardar_y_cargar_inventario():
    """Debe guardar y volver a cargar correctamente los productos."""
    data = [{"nombre": "Camisa", "precio": 50000, "cantidad": 10}]
    guardar_inventario(data)
    cargado = cargar_inventario()
    assert cargado == data

def test_agregar_producto(monkeypatch):
    """Debe agregar un producto correctamente."""
    inventario = []
    inputs = iter(["Gorra", "25000", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    agregar_producto(inventario)
    assert len(inventario) == 1
    assert inventario[0]["nombre"] == "Gorra"
    assert inventario[0]["precio"] == 25000.0
    assert inventario[0]["cantidad"] == 5

def test_vender_producto(monkeypatch, capsys):
    """Debe disminuir cantidad al vender un producto."""
    inventario = [{"nombre": "Pantalón", "precio": 80000, "cantidad": 5}]
    guardar_inventario(inventario)

    inputs = iter(["Pantalón", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    vender_producto(inventario)

    assert inventario[0]["cantidad"] == 3
    salida = capsys.readouterr().out
    assert "Venta realizada" in salida

def test_vender_producto_no_encontrado(monkeypatch, capsys):
    """Debe mostrar error si el producto no existe."""
    inventario = [{"nombre": "Camisa", "precio": 40000, "cantidad": 3}]
    inputs = iter(["Zapatos", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    vender_producto(inventario)
    salida = capsys.readouterr().out
    assert "Producto no encontrado" in salida

def test_mostrar_inventario(capsys):
    """Debe mostrar la tabla de inventario con rich."""
    inventario = [
        {"nombre": "Camisa", "precio": 40000, "cantidad": 3},
        {"nombre": "Pantalón", "precio": 80000, "cantidad": 5},
    ]
    mostrar_inventario(inventario)
    salida = capsys.readouterr().out
    assert "Camisa" in salida
    assert "Pantalón" in salida
