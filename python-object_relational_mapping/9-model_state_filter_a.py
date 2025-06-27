#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Conexión al servidor MySQL
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

    # Query con filtro de 'a' y ordenado por id
    states_with_a = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)

    # Mostrar resultados
    for state in states_with_a:
        print(f"{state.id}: {state.name}")
