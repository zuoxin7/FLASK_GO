from flask_wtf import FlaskForm, Form
from wtforms import SubmitField, TextAreaField, StringField, FileField,HiddenField, SelectField
from wtforms.validators import DataRequired
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from flask_wtf.file import FileRequired, FileAllowed


class VideoForm(FlaskForm):
    title = StringField(u"标题", validators=[Required()])
    hyperlink = StringField(u'超链接', validators=[Required()])
    # category = SelectField(u'上传类型', choices=[('1', '视频'),('2', '视频地址')])
    # video = FileField('请上传视频(mp4)',
    #                   validators=[FileRequired(), FileAllowed(['mp4'], '只允许上传mp4视频!')])
    image = FileField('请上传视频代表图片(jpg、png、jpeg)',
                      validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], '只允许上传图片!')])
    submit = SubmitField(u"发布")