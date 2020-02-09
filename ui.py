from flask import *
from flask_wtf import FlaskForm
import json

from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length, InputRequired

# from main import *



app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.Config')



class DonorForm(FlaskForm):
    """Contact form."""
    name = StringField('Your Organization Name', [
        InputRequired(), DataRequired()])
    address = StringField('Your Organization Address', [
        InputRequired(), DataRequired()])
    email = StringField('Email', [
        InputRequired(), DataRequired()])
    
    tel = TextField('Your Telephone Number', [
        DataRequired(), InputRequired(),
        Length(10, message=('Not a valid phone number'))])
    supplyType = StringField('Type of Supply', [InputRequired(), DataRequired()])
    supplyNumber = StringField('Number of Supply', [InputRequired(), DataRequired()])

    submit = SubmitField('Submit')

class SeekerForm(FlaskForm):
    """Contact form."""
    name = StringField('Your Organization Name', [
        InputRequired(), DataRequired()])
    address = StringField('Your Organization Address', [
        InputRequired(), DataRequired()])
    email = StringField('Email', [
        InputRequired(), DataRequired()])
    
    tel = TextField('Your Telephone Number', [
        DataRequired(), InputRequired(),
        Length(10, message=('Not a valid phone number'))])
    supplyType = StringField('Type of Supply', [InputRequired(), DataRequired()])
    supplyNumber = StringField('Number of Supply', [InputRequired(), DataRequired()])

    submit = SubmitField('Submit')




@app.route('/', methods=('GET', 'POST'))
def index():
    donorForm = DonorForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    # locList = returnLocList()

    return render_template('index.html', 

    form=donorForm)


if __name__ == "__ui__":
    app.run(debug=True)