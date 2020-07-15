from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SongSubmitForm(FlaskForm):
    titlename = StringField('Song Title')
    artistname = StringField('Artist Name')

    submit = SubmitField('Enter!')