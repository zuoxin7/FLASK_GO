from flask import render_template, session, redirect, url_for
from flask_login import login_required, current_user
from . import main
from ..models import User, Post, Video, Know, New
from .forms import PostForm


@main.route('/', methods=['GET', 'POST'])
def index():
    shipins = Video.select().where(Video.id <= 4)
    zhishis = Know.select().where(Know.log == 3)
    baiwens = Know.select().where(Know.log == 4)
    news = New.select().where(New.id <= 4)
    return render_template('index.html', shipins=shipins, zhishis=zhishis, baiwens=baiwens, news=news)

@main.route('/message', methods=['GET', 'POST'])
def message():
    form = PostForm()
    if (current_user.is_authenticated and form.validate_on_submit()):
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        post.save()
        return redirect(url_for('.message'))
    posts = Post.select().order_by(Post.timestamp.desc())
    return render_template('messagepush.html', form=form, posts=posts)
