from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('Leadership', validators=[DataRequired()])
    dropdown = SelectField('Choose an option', choices=['S8:G8:S9:G9:MELEE:FLY:MOUNT:RANGE','S8:S9:G8:G9:MELEE:MOUNT:RANGE:FLY', 'S8:S9:G8:G9:MELEE:FLY:MOUNT:RANGE','SKADI:G7:G8:G9:S9:MELEE:FLY:MOUNT:RANGE'])
    submit = SubmitField('Submit')
