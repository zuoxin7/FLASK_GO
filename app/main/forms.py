from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired



class PostForm(FlaskForm):
    body = TextAreaField(u'内容', validators=[DataRequired(u'内容不能为空')])
    submit = SubmitField('Submit')