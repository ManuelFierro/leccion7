import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine('postgres://postgres:admin@localhost:5432/aerolinea')
db = scoped_session(sessionmaker(bind=engine))


def main():
    vuelos = db.execute("SELECT origen, destino, duracion FROM vuelos").fetchall()
    for vuelo in vuelos:
        print("{vuelo.origen} a {vuelo.destino}, {vuelo.duracion} minutos.")


if __name__ == "__main__":
    main()
