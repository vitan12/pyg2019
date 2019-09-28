from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FieldList, IntegerField, FormField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ItemEntryForm(FlaskForm):
    name = StringField('Item name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    x = ['Clothing', 'Food', 'Cleaning', 'Misc.']
    dropdown_list = [(f, f) for f in x]
    cat_select = SelectField(label='Category', choices=dropdown_list, validators=[DataRequired()])
    submit = SubmitField('Create Item')
