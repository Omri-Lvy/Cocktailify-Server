from flask import request, jsonify
import json
from app.controllers.favorite_controller import handle_add_favorite, handle_remove_favorite

def register_routes(app):
    @app.route('/add-favorite', methods=['POST'])
    def add_to_favorites():
        request_data = request.get_json()
        data = json.loads(request_data)
        result, status_code = handle_add_favorite(data)
        return jsonify(result), status_code

    @app.route('/remove-favorite', methods=['POST'])
    def remove_from_favorites():
        request_data = request.get_json()
        data = json.loads(request_data)
        result, status_code = handle_remove_favorite(data)
        return jsonify(result), status_code