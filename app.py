
from flask import Flask, jsonify, request

app = Flask(__name__)

# "Base de datos" en memoria (marcas de motos)
marcas = [
    {"id": 1, "nombre": "Harley-Davidson"},
    {"id": 2, "nombre": "Triumph"}
]

# ✅ Endpoint tipo health (lo adaptamos a motos)
@app.route("/motos")
def motos():
    return jsonify({"status": "Ok"})

# ✅ GET - listar marcas
@app.route("/marcas", methods=["GET"])
def get_marcas():
    return jsonify(marcas)

# ✅ POST - crear marca
@app.route("/marcas", methods=["POST"])
def create_marca():
    data = request.get_json()

    nueva_marca = {
        "id": len(marcas) + 1,
        "nombre": data.get("nombre")
    }

    marcas.append(nueva_marca)
    return jsonify(nueva_marca), 201

# ✅ PUT - modificar marca
@app.route("/marcas/<int:marca_id>", methods=["PUT"])
def update_marca(marca_id):
    data = request.get_json()

    for marca in marcas:
        if marca["id"] == marca_id:
            marca["nombre"] = data.get("nombre")
            return jsonify(marca)

    return jsonify({"error": "Marca no encontrada"}), 404

# ✅ DELETE - eliminar marca
@app.route("/marcas/<int:marca_id>", methods=["DELETE"])
def delete_marca(marca_id):
    for marca in marcas:
        if marca["id"] == marca_id:
            marcas.remove(marca)
            return jsonify({"mensaje": "Marca eliminada"})

    return jsonify({"error": "Marca no encontrada"}), 404

# ✅ Home
@app.route("/")
def home():
    return "API de motos 🏍️ funcionando correctamente"

if __name__ == "__main__":
    app.run(debug=True)
