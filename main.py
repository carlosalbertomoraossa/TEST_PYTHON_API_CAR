from flask import Flask, jsonify
from app.controller.item_controller import ItemController

app = Flask(__name__)

item_controller: ItemController = ItemController()

# Endpoint to get a list of items
@app.route('/items', methods=['GET'])
def get_items_route():
    return jsonify(item_controller.get_items())

# Endpoint to get details about a specific item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item_route(item_id):
    return jsonify(item_controller.get_item(item_id))


if __name__ == '__main__':
    app.run(debug=True, port=8080)
