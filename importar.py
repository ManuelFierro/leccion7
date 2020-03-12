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
# solicitar que el usuario elija un vuelo
    vuelos_id = int(input("\n Vuelo ID: "))
    vuelos = db.execute("SELECT origen, destino, duracion FROM vuelos WHERE id = :id",
                        {"id": vuelos_id}).fetchone()
    print(
        f"El vuelo elejido es el numero: {vuelos_id}, de {vuelos.origen} a {vuelos.destino} con una duracion de {vuelos.duracion} minutos")
    # asegurar que el vuelo sea valido
    if vuelos is None:
        print("ERROR EL VUELO NO EXISTE")
        return


if __name__ == "__main__":
    main()
