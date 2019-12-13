from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class CreateBlog(FlaskForm):
    title = StringField(validators=[DataRequired(message="Title is a required field")])
    content = TextAreaField(validators=[DataRequired(message="Content is a required field")])


class EditBlog(CreateBlog):
    pass
