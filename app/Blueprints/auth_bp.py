from flask import Blueprint
from app.views.AuthView import logout, register, login


auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/register', methods=['GET', 'POST'])(register)
auth_bp.route('/login', methods=['GET', 'POST'])(login)
auth_bp.route('/logout', methods=['GET', 'POST'])(logout)