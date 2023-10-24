import json
from flask import Flask, request, render_template, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Carga de datos
with open("response.json", "r") as file:
    response = json.load(file)

# Ruta para cargar la plantilla HTML (inicio)
@app.route("/")
def template():
    return render_template("index.html")

# Procesamiento de solicitud POST
@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("user_input", "")
    response_text = response.get(user_input, "Lo siento, no pude entenderte. ¿Podrías reformular tu pregunta?")
    return jsonify({"respuesta": response_text})

# Ruta para servir archivos estáticos
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run()
