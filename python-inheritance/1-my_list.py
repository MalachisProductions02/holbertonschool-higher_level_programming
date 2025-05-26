#!/usr/bin/python3
"""
Este módulo define la clase MyList que hereda de list.
"""


class MyList(list):
    """
    Clase que hereda de list e incluye un método para imprimir la lista ordenada.
    """

    def print_sorted(self):
        """
        Imprime la lista ordenada (sin modificar la original).
        """
        print(sorted(self))
