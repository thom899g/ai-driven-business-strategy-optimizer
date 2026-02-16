from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/strategies', methods=['GET'])
def get_strategies():
    # Assume strategies are fetched from the model
    strategies = ["Strategy A", "