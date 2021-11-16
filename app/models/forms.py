from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user=StringField('user',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField()

class LoginTask(FlaskForm):
    task=StringField('Add new task',validators=[DataRequired()])
    submit=SubmitField()
class DeleteForm(FlaskForm):
    submit=SubmitField('Delete task')
class UpdateTaskForm(FlaskForm):
    submit=SubmitField('Change status')
