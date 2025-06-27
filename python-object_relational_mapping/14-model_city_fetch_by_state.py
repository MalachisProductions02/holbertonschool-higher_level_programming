#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    # Consultar y hacer join entre City y State, ordenando por City.id
    query = session.query(City, State).join(State).order_by(City.id)

    for city, state in query.all():
        print(f"{state.name}: ({city.id}) {city.name}")
