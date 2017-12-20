from flask_wtf import FlaskForm, Form
from wtforms import SubmitField, TextAreaField, StringField, SelectField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from flask_wtf.file import FileRequired, FileAllowed


class KnowForm(FlaskForm):
    title = StringField(u"标题", validators=[Required()])
    log = SelectField(u'类别', choices=[('1', '围棋知识'), ('2', '学棋百问')])
    content = TextAreaField(u"正文", validators=[Required()], id="_ckeditor")
    submit = SubmitField(u"发布")