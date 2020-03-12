import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv('DATABASE_URL'))
db = scoped_session(sessionmaker(bind=engine))

# listar vuelos


@app.route("/")
def index():
    vuelos = db.execute("SELECT * FROM vuelos").fetchall()
    return render_template("index.html", vuelos=vuelos)


@app.route("/book", methods=["POST"])
def book():
    """ Reserva un vuelo """
    nombre = request.form.get("nombre")
    try:
        vuelo_id = int(request.form.get("vuelo_id"))
    except ValueError:
        return render_template("error.html", message="Numero de vuelo invalido")
    # IF para ver si existe el vuelo
    if db.execute("SELECT * FROM vuelos WHERE id= :id", {"id": vuelo_id}).rowcount == 0:
        return render_template("error.html", message="No hay vuelo con ese ID")
    db.execute("INSERT INTO pasajeros (nombre,vuelo_id) VALUES (:nombre, :vuelo_id)",
               {"nombre": nombre, "vuelo_id": vuelo_id})
    db.commit()
    return render_template("success.html")


@app.route("/vuelos")
def vuelos():
    """ Listado de los vuelos """
    vuelos = db.execute("SELECT * FROM vuelos").fetchall()
    return render_template("vuelos.html", vuelos=vuelos)


@app.route("/vuelo/<int:vuelo_id>")
def vuelo(vuelo_id):
    """ Listado de los detalles del vuelo """
    vuelo = db.execute("SELECT * FROM vuelos WHERE id = :id", {"id": vuelo_id}).fetchone()
    if vuelo is None:
        return render_template("error.html", message="No existe ese vuelo")
    pasajeros = db.execute("SELECT * FROM pasajeros WHERE vuelo_id = :vuelo_id",
                           {"vuelo_id": vuelo_id}).fetchall()
    return render_template("vuelo.html", vuelo=vuelo, pasajeros=pasajeros)
