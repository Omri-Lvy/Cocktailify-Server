import requests

sent_cocktails_ids = set()
sent_cocktails = {}


def fetch_cocktail():
    url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
    response = requests.get(url)
    cocktail = response.json()['drinks'][0]
    return cocktail


def get_cocktails(page, batch_size):
    global sent_cocktails
    cocktails = []
    tries = 0
    cocktails_list = list(sent_cocktails.values())
    if len(sent_cocktails) >= batch_size * (page + 1):
        return cocktails_list[page * batch_size:(page + 1) * batch_size]
    while len(cocktails) < batch_size and tries < batch_size * (page + 2):
        cocktail = fetch_cocktail()
        if not sent_cocktails_ids.__contains__(cocktail['idDrink']):
            cocktails.append(cocktail)
            sent_cocktails_ids.add(cocktail['idDrink'])
            sent_cocktails[cocktail['strDrink']] = cocktail
        tries += 1
    return cocktails


def get_cocktail_by_name(name):
    cocktail = sent_cocktails.get(name)
    if cocktail:
        return cocktail
    url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={name}'
    response = requests.get(url)
    return response.json()['drinks'][0]


def search_cocktails(query):
    url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={query}'
    response = requests.get(url)
    return response.json()['drinks'] or []


def search_cocktails_by_category(category):
    if category == 'general':
        category = "other / unknown"
    category = category.replace('-', '/')
    url = f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?c={category}'
    response = requests.get(url)
    return response.json()['drinks'] or []


def search_cocktails_by_alcoholic(alcoholic):
    url = f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?a={alcoholic}'
    response = requests.get(url)
    print(len(response.json()['drinks']))
    return response.json()['drinks'] or []
