from flask import Flask, request

app = Flask(__name__)


# @app.route("/", methods=["GET", "POST"])
@app.route("/", methods=["POST"])
def hello_world():
    if request.method == "POST":
        return "Hello, POST request!"
    if request.method == "GET":
        return "Hello, GET request!"

    else:
        return "NO SE EJECUTAN METODOS"


if __name__ == "__main__":
    app.run()
