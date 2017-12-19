from flask import render_template, session, redirect, url_for
from flask_login import login_required, current_user
from . import new
from ..models import User, Post


@new.route('/new', methods=['GET', 'POST'])
def new():
    return render_template('new.html')