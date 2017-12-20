from flask import render_template, session, redirect, url_for, flash
from flask_login import login_required, current_user
from . import new
from ..models import User, Post, New
from .forms import NewForm
from werkzeug.utils import secure_filename

@new.route('/new', methods=['GET', 'POST'])
def news():
    news = New.select()
    return render_template('new.html', news=news)

@new.route('/push_new', methods=['GET', 'POST'])
def push_new():
    form = NewForm()
    if form.validate_on_submit():
        print('wocao')
        filename = secure_filename(form.image.data.filename)
        form.image.data.save('app/static/upload/' + filename)
        new = New(title=form.title.data,
                  content=form.content.data,
                  author=current_user._get_current_object(),
                  imagefile=secure_filename(form.image.data.filename))
        print('123')
        try:
            new.save()
            flash('你已经发布成功')
            return redirect('./new')
        except:
            flash("发布失败")
    return render_template('push.html', form=form)