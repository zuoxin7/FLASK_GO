from flask import Blueprint

new = Blueprint('new', __name__)

from . import views
