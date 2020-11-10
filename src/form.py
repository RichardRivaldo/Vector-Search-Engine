from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField , MultipleFileField
from wtforms.validators import DataRequired

class QueryForm(FlaskForm) :
    query = StringField('Query' , validators=[DataRequired()])
    submit = SubmitField('Search')

class UploadForm(FlaskForm) :
    file = MultipleFileField('File')
    submit = SubmitField('Submit')

