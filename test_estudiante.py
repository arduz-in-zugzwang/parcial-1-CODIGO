"""Escriba aquí sus pruebas. No borre ni modifique tests/test_base.py.

Cada función de prueba comienza con test_ y usa assert.
Agregue al menos los cuatro casos descritos en el README.
Los imports ya están preparados; deepcopy crea una copia independiente
de la lista y de los diccionarios para comprobar que no se modificaron.
"""
from copy import deepcopy

from reservas import modificar_reserva


# Ejemplo de estructura, sin solución del caso:
def test_nombre_del_comportamiento():
    datos = [dict(id="R1", sala="A", inicio=540, fin=600,
                  estado="confirmada")]
    antes = deepcopy(datos)
    resultado = modificar_reserva(datos, "R1",600, 660)
    assert resultado == "OK"
    # assert datos == antes  # Cuando la operación debe conservar TODO.

def test_genera_conflicto():
    datos = [dict(id="R1", sala="A", inicio=540, fin=600,
                  estado="confirmada")]
    antes = deepcopy(datos)
    resultado = modificar_reserva(datos, "R1", 600, 600)
    assert  resultado == "CONFLICTO"

def test_genera_conflicto_2():
    datos = [dict(id="R1", sala="A", inicio=540, fin=600,
                  estado="confirmada")]
    datos2 = [dict(id="R1", sala="A", inicio=600, fin=630,
                  estado="confirmada")]
    antes = deepcopy(datos)
    resultado = modificar_reserva(datos2, "R1", 600, 1339)
    assert  resultado == "OK"
