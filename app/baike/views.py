from flask import render_template, session, redirect, url_for
from flask_login import login_required, current_user
from . import baike
from ..models import User, Post


@baike.route('/baike', methods=['GET', 'POST'])
def baike():
    return render_template('baike.html')