from flask import request, jsonify
import json
from app.controllers.auth_controller import handle_register, handle_login

def register_routes(app):
    @app.route('/register', methods=['POST'])
    def register():
        request_data = request.get_json()
        data = json.loads(request_data)
        result, status_code = handle_register(data)
        return jsonify(result), status_code

    @app.route('/login', methods=['POST'])
    def login():
        request_data = request.get_json()
        data = json.loads(request_data)
        result, status_code = handle_login(data)
        return jsonify(result), status_code