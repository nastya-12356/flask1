from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class NewsJob(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    id = IntegerField('Team Leader id', validators=[DataRequired()])
    work_size = IntegerField('Work Size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_job_finished = BooleanField('Job Finished')
    submit = SubmitField('Submit')
    categories = SelectField('Category', coerce=int, validators=[DataRequired()])