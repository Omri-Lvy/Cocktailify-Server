from flask import request, redirect, url_for
from app.controllers.cocktail_controller import (
    handle_explore,
    handle_cocktail_details,
    handle_search,
    handle_category_search,
    handle_type_search
)

def register_routes(app):
    @app.route('/explore', methods=['GET'])
    def explore_page():
        page = request.args.get('page', default=0, type=int)
        batch_size = request.args.get('batch_size', default=10, type=int)
        return handle_explore(page, batch_size)

    @app.route('/cocktail/<cocktail_name>', methods=['GET'])
    def cocktail_page(cocktail_name):
        return handle_cocktail_details(cocktail_name)

    @app.route('/search', methods=['GET'])
    def search_page():
        query = request.args.get('q')
        return handle_search(query)

    @app.route('/category/<category>', methods=['GET'])
    def search_by_category(category):
        return handle_category_search(category)

    @app.route('/<type>', methods=['GET'])
    def search_by_alcoholic(type):
        cocktails = handle_type_search(type)
        if cocktails is None:
            return redirect(url_for('explore_page'))
        return cocktails