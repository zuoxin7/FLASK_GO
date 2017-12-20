from flask_wtf import FlaskForm, Form
from wtforms import SubmitField, TextAreaField, StringField, FileField
from wtforms.validators import DataRequired
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from flask_wtf.file import FileRequired, FileAllowed


class NewForm(FlaskForm):
    title = StringField(u"标题", validators=[Required()])
    image = FileField('请上传文章图片(jpg、png、jpeg)',
                      validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], '只允许上传图片!')])
    content = TextAreaField(u"正文", validators=[Required()], id="_ckeditor")
    submit = SubmitField(u"发布")