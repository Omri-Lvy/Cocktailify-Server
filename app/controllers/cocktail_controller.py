from app.services.cocktails_service import (
    get_cocktails,
    get_cocktail_by_name,
    search_cocktails,
    search_cocktails_by_category,
    search_cocktails_by_alcoholic
)

def handle_explore(page=0, batch_size=10):
    return get_cocktails(page, batch_size)

def handle_cocktail_details(cocktail_name):
    return get_cocktail_by_name(cocktail_name)

def handle_search(query):
    return search_cocktails(query)

def handle_category_search(category):
    return search_cocktails_by_category(category)

def handle_type_search(type):
    if type == 'alcoholic-drinks':
        return search_cocktails_by_alcoholic('Alcoholic')
    elif type == 'non-alcoholic-drinks':
        return search_cocktails_by_alcoholic('Non_Alcoholic')
    return None