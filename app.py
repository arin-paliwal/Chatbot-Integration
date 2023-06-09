from flask import Flask, render_template, request, jsonify
from flask_cors import CORS # for integrating it with other every website
from chat import get_response
app = Flask(__name__)
CORS(app) # for linking

# not needed -- for cors
# @app.get("/")  # flask 2.0
# def index_get():
#     return render_template('base.html')


@app.post("/predict")
def predit():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
