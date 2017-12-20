from flask import render_template, session, redirect, url_for, flash
from flask_login import login_required, current_user
from . import baike
from ..models import User, Know
from .forms import KnowForm


@baike.route('/baike', methods=['GET', 'POST'])
def baikes():
    zhishis = Know.select().where(Know.log == 1)
    baiwens = Know.select().where(Know.log == 2)
    return render_template('baike.html', zhishis=zhishis, baiwens=baiwens)

@baike.route('/push_baike', methods=['GET', 'POST'])
def push_baike():
    form = KnowForm()
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

@baike.route('/baike_show/<baikeid>', methods=['GET', 'POST'])
def baike_show(baikeid):
    baikesshow = Know.select().where(Know.id == baikeid)
    for n in baikesshow:
        time=str(n.timestamp)[:19]
    return render_template('baikeshow.html', baikes=baikesshow,timestamp=time)