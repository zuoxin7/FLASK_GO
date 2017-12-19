from flask import Blueprint

baike = Blueprint('baike', __name__)

from . import views
