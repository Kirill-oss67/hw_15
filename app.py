from flask import Flask, jsonify
from utils import get_data

app = Flask(__name__)

@app.route('/<itemid>')
def my_app(itemid):
    animal = get_data(itemid)
    return jsonify(animal)

if __name__ == '__main__':
    app.run(debug=True, port=1005)
