from flask import Blueprint
from app.views.AuthView import register


auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/register', methods=['GET', 'POST'])(register)