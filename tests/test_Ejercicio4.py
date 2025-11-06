import pytest
from Ejercicio4 import aplicar_validador, email_validado, numero_valido

def test_email_validado_correctos():
    """
    Verifica que los correos con '@' y '.' sean válidos.
    """
    assert email_validado("usuario@gmail.com")
    assert email_validado("test@dominio.co")
    assert email_validado("persona@mail.edu")


def test_email_validado_incorrectos():
    """
    Verifica que los correos sin formato correcto sean inválidos.
    """
    assert not email_validado("usuariogmail.com")
    assert not email_validado("usuario@mail")
    assert not email_validado("usuario.com")


def test_numero_valido_correctos():
    """
    Verifica que los números mayores a 10 sean válidos.
    """
    assert numero_valido("11")
    assert numero_valido("69")
    assert numero_valido("1000")


def test_numero_valido_incorrectos():
    """
    Verifica que los números menores o iguales a 10 o inválidos sean rechazados.
    """
    assert not numero_valido("10")
    assert not numero_valido("5")
    assert not numero_valido("0")
    assert not numero_valido("abc")


def test_aplicar_validador_emails():
    """
    Verifica que aplicar_validador funcione correctamente con emails.
    """
    datos = ["a@gmail.com", "bmail.com", "c@hotmail.com"]
    resultado = aplicar_validador(datos, email_validado)
    assert resultado == ["a@gmail.com", "c@hotmail.com"]


def test_aplicar_validador_numeros():
    """
    Verifica que aplicar_validador funcione correctamente con números.
    """
    datos = ["5", "12", "20", "1"]
    resultado = aplicar_validador(datos, numero_valido)
    assert resultado == ["12", "20"]
