import json
import pytest
from Ejercicio15 import (
    cargar_biblioteca,
    guardar_biblioteca,
    prestar_libro,
    devolver_libro,
    buscar_libro,
    ver_libros_prestados,
    mostrar_libros_prestados,
)


@pytest.fixture
def sample_libros(tmp_path):
    archivo = tmp_path / "biblioteca.json"
    datos = [
        {"libro_id": "001", "titulo": "Cien Años de Soledad", "prestado_a": None},
        {"libro_id": "002", "titulo": "El Aleph", "prestado_a": None},
        {"libro_id": "003", "titulo": "Sapiens", "prestado_a": "Marta"},
    ]
    archivo.write_text(
        json.dumps(datos, ensure_ascii=False, indent=4), encoding="utf-8"
    )
    return archivo


def test_cargar_guardar(tmp_path, sample_libros):
    ruta = sample_libros
    libros = cargar_biblioteca(str(ruta))
    assert isinstance(libros, list)
    assert len(libros) == 3

    libros[0]["prestado_a"] = "Juan"
    guardar_biblioteca(libros, str(ruta))
    recargado = cargar_biblioteca(str(ruta))
    assert recargado[0]["prestado_a"] == "Juan"


def test_prestar_devolver(sample_libros):
    ruta = str(sample_libros)
    libros = cargar_biblioteca(ruta)

    ok = prestar_libro(libros, "002", "Pedro")
    assert ok is True
    assert next(l for l in libros if l["libro_id"] == "002")["prestado_a"] == "Pedro"

    nok = prestar_libro(libros, "003", "Carlos")
    assert nok is False

    ok2 = devolver_libro(libros, "003")
    assert ok2 is True
    assert next(l for l in libros if l["libro_id"] == "003")["prestado_a"] is None


def test_buscar_libro(sample_libros):
    ruta = str(sample_libros)
    libros = cargar_biblioteca(ruta)
    res = buscar_libro(libros, "aleph")
    assert len(res) == 1
    assert res[0]["titulo"] == "El Aleph"


def test_ver_libros_prestados(sample_libros, capsys):
    ruta = str(sample_libros)
    libros = cargar_biblioteca(ruta)
    prestados = ver_libros_prestados(libros)
    assert len(prestados) == 1
    mostrar_libros_prestados(libros)
    salida = capsys.readouterr().out
    assert "Sapiens" in salida
