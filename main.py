from flask import Flask, jsonify, request, Response
import functools

app = Flask(__name__)


@app.route('/')
def index() -> str:
    with open('contents.html') as contents:
        return contents.read()


@app.route('/add', methods=['POST'])
def add() -> Response:
    data = request.get_json()
    return jsonify(
        total=sum(data),
    )


@app.route('/multiply', methods=['POST'])
def multiply() -> Response:
    data = request.get_json()
    product = functools.reduce(lambda a, b: a*b, data)
    return jsonify(
        product=product,
    )


@app.route('/minmax', methods=['POST'])
def minmax() -> Response:
    data = request.get_json()
    return jsonify(
        min=min(data),
        max=max(data),
    )
