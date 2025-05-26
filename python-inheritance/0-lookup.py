#!/usr/bin/python3
"""
Este módulo contiene la función 'lookup' que retorna
los atributos y métodos disponibles de un objeto.
"""


def lookup(obj):
    """
    Devuelve la lista de atributos y métodos disponibles de un objeto.
    """
    return dir(obj)
