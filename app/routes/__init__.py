from .auth_routes import register_routes as register_auth_routes
from .cocktail_routes import register_routes as register_cocktail_routes
from .favorite_routes import register_routes as register_favorite_routes

__all__ = [
    'register_auth_routes',
    'register_cocktail_routes',
    'register_favorite_routes'
]