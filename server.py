import json
from flask import Flask, request, render_template
from flask_cors import CORS


app = Flask(__name__)
url = "http://httpbin.org/post"
CORS(app)

# carga de datos
with open("response.json", "r") as file:
    response = json.load(file)


# prueb(inicio)
@app.route("/")
def template():
    return render_template("index.html")


# prueb(fin)


# procesamiento de solicitud POST
@app.route("/get_response", methods=["GET", "POST"])  # el problema esta en esta linea
def get_response():
    # obtener la entrada del usuario del cuerpo de la solicitud
    user_input = request.json["user_input"]
    # return "<h1> desde el servidor se ve solicitud del cliente: " + user_input + "</h1>"
    # buscar respuesta en datos
    if user_input in response:
        response = response[user_input]
        print("se muestra en el servidor usuario dijo:", user_input)
        print("se muestra en el servidor bot dijo:", user_input)
    else:
        response = "Lo siento, no pude entenderte. ¿Podrías reformular tu pregunta?"

    # enviar respuesta como JSON
    return {"respuesta": response}
    # return "estoy en el servidor", user_input


if __name__ == "__main__":
    app.run()
# https://www.youtube.com/watch?v=dlhg8HMZTOk
