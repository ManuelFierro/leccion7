import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv('DATABASE_URL'))
db = scoped_session(sessionmaker(bind=engine))

# listar vuelos


def main():
    vuelos = db.execute("SELECT id, origen, destino, duracion FROM vuelos").fetchall()
    for viaje in vuelos:
        print(f"Vuelo {viaje.id}: de {viaje.origen}: a {viaje.destino}, {viaje.duracion} minutos")
        db.commit()
# solicitar que el usuario elija un vuelo
    vuelo_id = int(input("\n Vuelo ID: "))
    vuelo = db.execute("SELECT id,origen, destino, duracion FROM vuelos WHERE id = :id",
                       {"id": vuelo_id}).fetchone()

    print(
        f"El vuelo elejido es el numero: {vuelo.id}, de {vuelo.origen} a {vuelo.destino} con una duracion de {vuelo.duracion} minutos")
    # asegurar que el vuelo sea valido
    if vuelo is None:
        print("ERROR EL VUELO NO EXISTE")
        return
    # lista de pasajeros
    pasajeros = db.execute("SELECT nombre FROM pasajeros WHERE vuelos_id = :vuelos_id",
                           {"vuelos_id": vuelo_id}).fetchall()
    print(f"\n Pasajeros: ")
    for pasajero in pasajeros:
        print(pasajero.nombre)
    if len(pasajeros) == 0:
        print("No hay pasajeros.")


if __name__ == "__main__":
    main()
