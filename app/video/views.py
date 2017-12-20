from flask import render_template, session, redirect, url_for
from flask_login import login_required, current_user
from . import video
from ..models import User, Post, Video
from .forms import VideoForm


@video.route('/video', methods=['GET', 'POST'])
def video():
    return render_template('video.html')

@video.route('/push_video', methods=['GET', 'POST'])
def push_video():
    form = VideoForm()
    if form.validate_on_submit():
        new = Know(title=form.title.data,
                   log=form.log.data,
                  content=form.content.data,
                  author=current_user._get_current_object())
        try:
            new.save()
            flash('你已经发布成功')
            return redirect('./baike')
        except:
            flash("发布失败")
    return render_template('pushKnow.html', form=form)