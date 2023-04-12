import json
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
url = "http://httpbin.org/post"
CORS(app)

# carga de datos
with open("response.json", "r") as file:
    response = json.load(file)


# procesamiento de solicitud POST
@app.route("/get_response", methods=["GET", "POST"])  # el problema esta en esta linea
def get_response():
    # obtener la entrada del usuario del cuerpo de la solicitud
    user_input = request.json["user_input"]

    # buscar respuesta en datos
    if user_input in response:
        response = response[user_input]
        print(user_input)
    else:
        response = "Lo siento, no pude entenderte. ¿Podrías reformular tu pregunta?"

    # enviar respuesta como JSON
    return {"respuesta": response}
    # return "estoy en el servidor", user_input


if __name__ == "__main__":
    app.run()
