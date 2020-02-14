from random import choice
from flask import Flask, jsonify
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
    return jsonify(nome=name_m)


@app.route("/feminino")
def names_f():
    name_f = choice(data_f)[:-1]
    return jsonify(nome=name_f)


if __name__ == "__main__":
    app.run()
