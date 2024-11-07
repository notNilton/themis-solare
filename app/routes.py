# app/routes.py

from flask import Blueprint

# Defina um blueprint se desejar organizar suas rotas
routes = Blueprint('routes', __name__)

# Defina uma rota como exemplo
@routes.route('/example')
def example_route():
    return "Esta é uma rota de exemplo"
