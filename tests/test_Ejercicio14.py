import os
import json
import csv
from Ejercicio14 import leer_csv, leer_json, generar_reporte


def crear_csv_prueba(nombre_archivo):
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "nombre"])
        writer.writeheader()
        writer.writerow({"id": "1", "nombre": "Ana"})
        writer.writerow({"id": "2", "nombre": "Carlos"})

def crear_json_prueba(nombre_archivo):
    data = [
        {"id_estudiante": "1", "nombre_curso": "Python"},
        {"id_estudiante": "1", "nombre_curso": "Git"},
        {"id_estudiante": "2", "nombre_curso": "Bases de Datos"},
    ]
    with open(nombre_archivo, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def test_leer_csv(tmp_path):
    archivo_csv = tmp_path / "estudiantes.csv"
    crear_csv_prueba(archivo_csv)
    datos = leer_csv(archivo_csv)
    assert len(datos) == 2
    assert datos[0]["nombre"] == "Ana"

def test_leer_json(tmp_path):
    archivo_json = tmp_path / "cursos.json"
    crear_json_prueba(archivo_json)
    datos = leer_json(archivo_json)
    assert len(datos) == 3
    assert datos[1]["nombre_curso"] == "Git"

def test_generar_reporte(tmp_path, capsys):
    archivo_csv = tmp_path / "estudiantes.csv"
    archivo_json = tmp_path / "cursos.json"
    archivo_reporte = tmp_path / "reporte.txt"

    crear_csv_prueba(archivo_csv)
    crear_json_prueba(archivo_json)

    estudiantes = leer_csv(archivo_csv)
    cursos = leer_json(archivo_json)

    generar_reporte(estudiantes, cursos, archivo_reporte)

    assert archivo_reporte.exists()

    contenido = archivo_reporte.read_text(encoding="utf-8")
    assert "Ana: Python, Git" in contenido
    assert "Carlos: Bases de Datos" in contenido

    salida = capsys.readouterr().out
    assert "Vista previa del reporte antes de guardar" in salida
    assert "Reporte guardado en" in salida
    assert "Python" in salida
    assert "Carlos" in salida
