#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Crear motor de conexión
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar todos los estados con 'a' en el nombre
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Eliminar los estados encontrados
    for state in states_to_delete:
        session.delete(state)

    # Guardar los cambios
    session.commit()
