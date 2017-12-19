from flask import render_template, session, redirect, url_for
from flask_login import login_required, current_user
from . import video
from ..models import User, Post


@video.route('/new', methods=['GET', 'POST'])
def video():
    return render_template('video.html')