from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms import validators
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about yourself', validators=[Required()])
    submit = SubmitField('Edit bio')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment here')
    submit = SubmitField('Comment')

    