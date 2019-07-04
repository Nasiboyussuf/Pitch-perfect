from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import TextAreaField,SubmitField,StringField

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Update bio.',validators = [Required()])
    submit = SubmitField('Save Changes')

class PostAPitch (FlaskForm):
    title = StringField('Title',validators = [Required()])
    content = TextAreaField('Pitch',validators = [Required()])
    submit = SubmitField('Pitch')

class PostAComment (FlaskForm):
    comment = TextAreaField(validators = [Required()])
    submit = SubmitField('Comment',validators = [Required()])