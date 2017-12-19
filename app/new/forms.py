from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField
from wtforms.validators import DataRequired
from wtforms.validators import Required, Length, Email, Regexp, EqualTo



class TitleForm(FlaskForm):
    title = StringField(u'标题', validators=[Required()])

class NewForm(FlaskForm):
    body = TextAreaField(u'内容', validators=[DataRequired(u'内容不能为空')])
    submit = SubmitField('Submit')