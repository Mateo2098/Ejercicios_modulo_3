from Ejercicio2 import crear_perfil

def test_crear_perfil_condatos():
    """
    Verifia que la función funcione correctamente con todos los datos
    """
    resultado=crear_perfil(
        "Carol",
        25,
        "Cocinar","Dormir",
        facebook="@carol",
        instagram="@carol"
    )

    assert "Carol" in resultado
    assert "Cocinar" in resultado
    assert "Dormir" in resultado

def test_crear_perfil_sindatos():
    """
    Verifica el comportamiento cuando no se ingresan hobbies ni redes
    """
    resultado=crear_perfil("Alejo",30 )
    assert "No especificados" in resultado
    assert "No registradas" in resultado




