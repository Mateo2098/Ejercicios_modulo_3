import os
import pytest
from Ejercicio11 import agregar_tarea, ver_tareas, ARCHIVO_TAREAS

@pytest.fixture(autouse=True)
def limpiar_archivo():
    if os.path.exists(ARCHIVO_TAREAS):
        os.remove(ARCHIVO_TAREAS)
    yield
    if os.path.exists(ARCHIVO_TAREAS):
        os.remove(ARCHIVO_TAREAS)

def test_agregar_y_ver_tarea():
    agregar_tarea("Estudiar Python")
    agregar_tarea("Tomar café ")
    tareas = ver_tareas()
    assert "Estudiar Python" in tareas
    assert "Tomar café " in tareas

def test_archivo_vacio():
    tareas = ver_tareas()
    assert tareas == []
