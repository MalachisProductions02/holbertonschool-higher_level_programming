#!/usr/bin/python3
"""
Script that adds all command line arguments to a Python list
and saves them to a file as JSON representation.
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # Intentamos cargar la lista existente
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # Si el archivo no existe, iniciamos una lista vacía
    my_list = []

# Añadimos todos los argumentos de la línea de comandos (sin contar el script)
my_list.extend(sys.argv[1:])

# Guardamos la lista actualizada en el archivo JSON
save_to_json_file(my_list, filename)
