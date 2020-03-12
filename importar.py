import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv('DATABASE_URL'))
db = scoped_session(sessionmaker(bind=engine))

# listar vuelos


def main():
    fo = open("vuelos.csv")
    lector = csv.reader(fo)
    for origen, destino, duracion in lector:
        db.execute("INSERT INTO vuelos (origen, destino, duracion) VALUES(:origen, :destino, :duracion)", {
                   "origen": origen, "destino": destino, "duracion": duracion})
        print(f"agregados vuelos desde {origen} a {destino} durando {duracion} minutos.")
    db.commit()


if __name__ == "__main__":
    main()
