from flask import render_template, session, redirect, url_for, flash
from flask_login import login_required, current_user
from . import video
from ..models import User, Post, Video
from .forms import VideoForm
from werkzeug.utils import secure_filename


@video.route('/video', methods=['GET', 'POST'])
def videos():
    shipins = Video.select()
    return render_template('video.html',shipins=shipins)

@video.route('/push_video', methods=['GET', 'POST'])
def push_video():
    form = VideoForm()
    if form.validate_on_submit():
        filename = secure_filename(form.image.data.filename)
        form.image.data.save('app/static/upload/' + filename)
        video = Video(title=form.title.data,
                      imagefile=filename,
                      hyperlink=form.hyperlink.data)
        try:
            video.save()
            flash('你已经发布成功')
            return redirect('./video')
        except:
            flash("发布失败")
    return render_template('pushVideo.html', form=form)