import pytest
from Ejercicio1 import calcular_imc, interpretar_imc


def test_calcular_imc_correcto():
    """
    Verifica que el IMC se calcule correctamente
    """
    resultado = calcular_imc(70, 1.75)
    assert round(resultado, 2) == 22.86


def test_calcular_imc_estatura_invalida():
    """
    Verifica que se de un error en la estatura
    """
    with pytest.raises(ValueError):
        calcular_imc(70, 0)


def test_interpretar_imc_bajo():
    imc = 17.0
    assert interpretar_imc(imc) == f"Su IMC es {round(imc, 2)}: Destrunido y re flaco."


def test_interpretar_imc_normal():
    imc = 22.0
    assert interpretar_imc(imc) == f"Su IMC es {round(imc, 2)}: usted esta una re chimba."


def test_interpretar_imc_sobrepeso():
    imc = 27.5
    assert interpretar_imc(imc) == f"Su IMC es {round(imc, 2)}: ojo con eso baje de peso."


def test_interpretar_imc_obesidad():
    imc = 31.5
    assert interpretar_imc(imc) == f"Su IMC es {round(imc, 2)}: no le llama la atension un gym o una cirugia?."
