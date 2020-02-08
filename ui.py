from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length, InputRequired
from back import *



app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')
app.config['RECAPTCHA_PUBLIC_KEY'] = 'iubhiukfgjbkhfvgkdfm'
app.config['RECAPTCHA_PARAMETERS'] = {'size': '100%'}


class DonorForm(FlaskForm):
    """Contact form."""
    name = StringField('Your Organization Name', [
        InputRequired(), DataRequired()])
    address = StringField('Your Organization Address', [
        InputRequired(), DataRequired()])
    email = StringField('Email', [
        Email(message=('Not a valid email address.')),
        InputRequired, DataRequired()])
    
    tel = TextField('Your Telephone Number', [
        DataRequired(), InputRequired(),
        Length(10, message=('Not a valid phone number'))])
    supplyType = StringField('Type of Supply', [InputRequired(), DataRequired()])
    supplyNumber = StringField('Number of Supply', [InputRequired(), DataRequired()])

    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

class SeekerForm(FlaskForm):
    """Contact form."""
    name = StringField('Name', [
        DataRequired()])
    email = StringField('Email', [
        Email(message=('Not a valid email address.')),
        DataRequired()])
    body = TextField('Message', [
        DataRequired(),
        Length(min=4, message=('Your message is too short.'))])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')




@app.route('/', methods=('GET', 'POST'))
def index():
    donorForm = DonorForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    locList = returnLocList()

    return render_template('index.html', 

    form=form, locList = locList, )


if __name__ == "__main__":
    app.run(debug=True)