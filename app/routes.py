from flask import request, redirect, url_for
from app import app
from app.models.user import User
from app.services.cocktails_service import get_cocktails, get_cocktail_by_name, search_cocktails, \
    search_cocktails_by_category, search_cocktails_by_alcoholic


@app.route('/')
def index():
    return 'Hello, Omri!'


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    user = User(name, email, password)
    user.register()
    return 'User registered!'


@app.route('/login', methods=['GET'])
def login():
    name = request.form['name']
    password = request.form['password']
    if User.login(name, password):
        return 'User logged in!'
    return 'Invalid username or password'


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
