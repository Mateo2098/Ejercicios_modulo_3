import pytest
from Ejercicio7 import estudiantes_aprovados


def test_estudiantes_aprovados_basico():
    """
    Verifica que solo los estudiantes con nota >= 3.0 sean aprobados.
    """
    estudiantes = [
        ("Ana", 2.5),
        ("Juan", 2.8),
        ("Maria", 3.9),
        ("Andres", 4.5),
        ("Carlitos", 2.9),
        ("El klk", 5.0),
    ]
    resultado = estudiantes_aprovados(estudiantes)
    nombres = [e[0] for e in resultado]

    assert "Maria" in nombres
    assert "Andres" in nombres
    assert "El klk" in nombres
    assert "Ana" not in nombres
    assert "Juan" not in nombres
    assert "Carlitos" not in nombres


def test_estudiantes_aprovados_vacio():
    """
    Verifica que si nadie aprueba, la lista esté vacía.
    """
    estudiantes = [("Pedro", 2.0), ("Laura", 1.9)]
    resultado = estudiantes_aprovados(estudiantes)
    assert resultado == []


def test_estudiantes_aprovados_todos():
    """
    Verifica el comportamiento cuando todos aprueban.
    """
    estudiantes = [("A", 3.0), ("B", 3.5), ("C", 5.0)]
    resultado = estudiantes_aprovados(estudiantes)
    assert len(resultado) == 3
