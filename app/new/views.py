from flask import render_template, session, redirect, url_for, flash, request
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
        filename = secure_filename(form.image.data.filename)
        form.image.data.save('app/static/upload/' + filename)
        new = New(title=form.title.data,
                  content=form.content.data,
                  author=current_user._get_current_object(),
                  imagefile=filename)
        try:
            new.save()
            flash('你已经发布成功')
            return redirect('./new')
        except:
            flash("发布失败")
    return render_template('pushNew.html', form=form)

@new.route('/new_show/<newid>', methods=['GET', 'POST'])
def new_show(newid):
    newsshow = New.select().where(New.id == newid)
    for n in newsshow:
        time=str(n.timestamp)[:19]
    return render_template('newshow.html', news=newsshow,timestamp=time)