from flask_wtf import FlaskForm, Form
from wtforms import SubmitField, TextAreaField, StringField, FileField,HiddenField, SelectField
from wtforms.validators import DataRequired
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from flask_wtf.file import FileRequired, FileAllowed


class NewForm(FlaskForm):
    title = StringField(u"标题", validators=[Required()])
    category = SelectField(u'上传类型', choices=[('1', '视频'),('2', '视频地址')])
    video = FileField('请上传视频(mp4)',
                      validators=[FileRequired(), FileAllowed(['mp4'], '只允许上传mp4视频!')])

    content = TextAreaField(u"正文", validators=[Required()], id="_ckeditor")
    submit = SubmitField(u"发布")