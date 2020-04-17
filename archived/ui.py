from flask import *
from flask_wtf import FlaskForm
import json
from flask_wtf.csrf import CSRFProtect

from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length, InputRequired

import os
SECRET_KEY = os.urandom(32)


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.Config')
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = SECRET_KEY

class DonorForm(FlaskForm):
    """Contact form."""
    csrf = True
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
    csrf = True
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




@app.route('/', methods=['GET', 'POST'])
def index():
    donorForm = DonorForm()
    seekerForm = SeekerForm()
    # return redirect({{ url_for('static',filename='templates/success.html') }})
    # locList = returnLocList()
    if request.method == 'POST':
        if seekerForm.validate_on_submit():
            data = extractUserInfoSeeker(seekerForm)
            return url_for('seekerSuccess', name=data['name'])
    else: 
        return render_template('index.html', 
        donorForm=donorForm, seekerForm = seekerForm)



@app.route('/donorSuccess', methods=['GET', 'POST'])
def donorSuccess():
    # return redirect(url_for('success'))
    # # locList = returnLocList()
    
    return render_template('seekerSuccess.html')

@app.route('/seekerSuccess', methods=['GET', 'POST'])
def seekerSuccess(name):
    # return redirect(url_for('success'))
    # # locList = returnLocList()
    return render_template('seekerSuccess.html', name=name)




# data management helper functions

def extractUserInfoSeeker(formData):
    name = formData.name.data
    email = formData.email.data
    address = formData.address.data
    tel = formData.tel.data
    supplyType = formData.supplyType.data
    supplyNumber = formData.supplyNumber.data
    dic = [['type', 'seeker'],
           ['name', name],
           ['supplyType', supplyType],
           ['supplyNumber', supplyNumber],
           ['addr', address],
           ['tel', tel],
           ['email', email],
           ['info', 'placeholder in construction']
           ]
    return json.dumps(dic)

if __name__ == "__ui__":
    app.run(debug=True)

