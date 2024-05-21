from flask import request, redirect, url_for, jsonify
import json
from app import app
from app.models.user import User
from app.services.cocktails_service import get_cocktails, get_cocktail_by_name, search_cocktails, \
    search_cocktails_by_category, search_cocktails_by_alcoholic


@app.route('/register', methods=['POST'])
def register():
    try:
        request_data = request.get_json()
        data = json.loads(request_data)
        if not data:
            return jsonify({'isSuccess': False, 'message': 'No data provided'}), 400

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        # Ensure all required fields are provided
        if not all([name, email, password]):
            return jsonify({'isSuccess': False, 'message': 'Missing required fields'}), 400
        user = User(name, email, password, [])
        isSuccess, user = user.register()
        message = 'User registered successfully' if isSuccess else 'User already exists'
        results = {
            'isSuccess': isSuccess,
            'message': message,
            'user': {
                'id': user['_id'],
                'favorites': user['favorites']
            }
        }
        return jsonify(results), 200 if isSuccess else 400
    except RuntimeError:
        return jsonify({'isSuccess': False, 'message': 'Server Error occurred'}), 500


@app.route('/login', methods=['POST'])
def login():
    try:
        request_data = request.get_json()
        data = json.loads(request_data)
        if not data:
            return jsonify({'isSuccess': False, 'message': 'No data provided'}), 400
        email = data.get('email')
        password = data.get('password')
        isSuccess, user = User.login(email, password)
        if user:
            results = {
                'isSuccess': isSuccess,
                'message': 'User logged in!' if isSuccess else 'Email or password is incorrect',
                'user': {
                    'id': str(user['_id']),
                    'favorites': user['favorites']
                }
            }
        else:
            results = {
                'isSuccess': isSuccess,
                'message': 'Email or password is incorrect',
                'user': None
            }
        return jsonify(results), 200 if isSuccess else 400
    except RuntimeError:
        return jsonify({'isSuccess': False, 'message': 'Server Error occurred'}), 500


@app.route('/explore', methods=['GET'])
def explore_page():
    page = request.args.get('page', default=0, type=int)
    batch_size = request.args.get('batch_size', default=10, type=int)
    cocktails = get_cocktails(page, batch_size)

    return cocktails


@app.route('/cocktail/<cocktail_name>', methods=['GET'])
def cocktail_page(cocktail_name):
    cocktail = get_cocktail_by_name(cocktail_name)
    return cocktail


@app.route('/search', methods=['GET'])
def search_page():
    query = request.args.get('q')
    search_results = search_cocktails(query)
    return search_results


@app.route('/category/<category>', methods=['GET'])
def search_by_category(category):
    cocktails = search_cocktails_by_category(category)
    return cocktails


@app.route('/<type>', methods=['GET'])
def search_by_alcoholic(type):
    match type:
        case 'alcoholic-drinks':
            cocktails = search_cocktails_by_alcoholic('Alcoholic')
        case 'non-alcoholic-drinks':
            cocktails = search_cocktails_by_alcoholic('Non_Alcoholic')
        case _:
            return redirect(url_for('explore_page'))
    return cocktails


@app.route('/add-favorite', methods=['POST'])
def add_to_favorites():
    try:
        request_data = request.get_json()
        data = json.loads(request_data)
        if not data:
            return jsonify({'isSuccess': False, 'message': 'No data provided'}), 400
        user_id = data.get('user_id')
        cocktail = data.get('cocktail')
        isSuccess, message = User.add_to_favorites(user_id, cocktail)
        return jsonify({'isSuccess': isSuccess, 'message': message}), 200 if isSuccess else 400
    except RuntimeError:
        return jsonify({'isSuccess': False, 'message': 'Server Error occurred'}), 500


@app.route('/remove-favorite', methods=['POST'])
def remove_from_favorites():
    try:
        request_data = request.get_json()
        data = json.loads(request_data)
        if not data:
            return jsonify({'isSuccess': False, 'message': 'No data provided'}), 400
        user_id = data.get('user_id')
        cocktail = data.get('cocktail_id')
        isSuccess, message = User.remove_from_favorites(user_id, cocktail)
        return jsonify({'isSuccess': isSuccess, 'message': message}), 200 if isSuccess else 400
    except RuntimeError:
        return jsonify({'isSuccess': False, 'message': 'Server Error occurred'}), 500
