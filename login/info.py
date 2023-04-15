from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, PasswordField, DecimalField, \
                    DecimalRangeField, SelectField, RadioField, IntegerRangeField
from wtforms.validators import DataRequired, EqualTo, Email, NumberRange, InputRequired

class LoginForm(FlaskForm):
    username = StringField('Usersname', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in!')
    