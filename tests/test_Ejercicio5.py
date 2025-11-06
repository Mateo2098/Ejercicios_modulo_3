import pytest
from Ejercicio5 import calculo_iva, actualizar_tasa, TASA_IVA


def test_calculo_iva_basico():
    """
    Verifica que el cálculo del IVA sea correcto con la tasa inicial.
    """
    valor_iva, total = calculo_iva(100)
    assert round(valor_iva, 2) == 19.00
    assert round(total, 2) == 119.00


def test_actualizar_tasa_cambia_global():
    """
    Verifica que actualizar_tasa modifique la tasa de IVA global.
    """
    actualizar_tasa(0.25)
    valor_iva, total = calculo_iva(100)
    assert round(valor_iva, 2) == 25.00
    assert round(total, 2) == 125.00


def test_calculo_iva_con_tasa_personalizada():
    """
    Verifica que con una tasa personalizada, los resultados sean correctos.
    """
    actualizar_tasa(0.10)
    valor_iva, total = calculo_iva(200)
    assert round(valor_iva, 2) == 20.00
    assert round(total, 2) == 220.00


def test_tasa_no_negativa():
    """
    Verifica que no se realicen cálculos incorrectos con tasas negativas.
    """
    actualizar_tasa(0.15)
    valor_iva, total = calculo_iva(0)
    assert valor_iva == 0
    assert total == 0
