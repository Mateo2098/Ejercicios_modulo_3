import csv
import os
import pytest
from Ejercicio12 import analizar_csv

ARCHIVO_PRUEBA = "datos_prueba.csv"


@pytest.fixture(autouse=True)
def crear_archivo_csv():
    datos = [
        {"nombre": "Ana", "edad": "20", "calificación": "4.5"},
        {"nombre": "Juan", "edad": "22", "calificación": "3.8"},
        {"nombre": "Sofía", "edad": "19", "calificación": "4.9"},
    ]
    with open(ARCHIVO_PRUEBA, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["nombre", "edad", "calificación"])
        writer.writeheader()
        writer.writerows(datos)
    yield
    os.remove(ARCHIVO_PRUEBA)


def test_analizar_csv_calificacion():
    resultados = analizar_csv(ARCHIVO_PRUEBA, "calificación")
    assert "Promedio" in resultados
    assert "Máximo" in resultados
    assert "Mínimo" in resultados
    assert round(resultados["Promedio"], 2) == 4.4
    assert resultados["Máximo"] == 4.9
    assert resultados["Mínimo"] == 3.8
