from flask import Blueprint
from app.views.HomeView import home


index_bp = Blueprint('index_bp', __name__)

index_bp.route('/', methods=['GET'])(home)