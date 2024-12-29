from .auth_controller import handle_login, handle_register
from .cocktail_controller import (
    handle_explore,
    handle_cocktail_details,
    handle_search,
    handle_category_search,
    handle_type_search
)
from .favorite_controller import handle_add_favorite, handle_remove_favorite

__all__ = [
    # Auth controller functions
    'handle_login',
    'handle_register',

    # Cocktail controller functions
    'handle_explore',
    'handle_cocktail_details',
    'handle_search',
    'handle_category_search',
    'handle_type_search',

    # Favorite controller functions
    'handle_add_favorite',
    'handle_remove_favorite'
]