import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


# sentencia carga motor bd directo
motor = create_engine("postgres://postgres:admin@localhost:5432/postgres")


# llama la variable de entorno, debe tener comillas simples
engine = create_engine(os.getenv('DATABASE_URL'))
db = scoped_session(sessionmaker(bind=engine))


def main():
    vls = db.execute("SELECT origen, destino, duracion FROM vuelos").fetchall()
    for vuelo in vls:
        print(f"{vuelo.origen} a {vuelo.destino}, {vuelo.duracion} minutos.")


if __name__ == "__main__":
    main()
