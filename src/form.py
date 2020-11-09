from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField
from wtforms.validators import DataRequired

class QueryForm(FlaskForm) :
    query = StringField('Query' , validators=[DataRequired()])
    submit = SubmitField('Search')

