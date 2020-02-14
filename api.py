from random import choice
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


with open("names-m.txt", "r") as f:
    data_m = f.readlines()


with open("names-f.txt", "r") as f:
    data_f = f.readlines()


@app.route("/masculino")
def names_m():
    name_m = choice(data_m)[:-1]

    return { 'name': name_m }, 200


@app.route("/feminino")
def names_f():
    name_f = choice(data_f)[:-1]

    return { 'nome': name_f }, 200


if __name__ == "__main__":
    app.run()
