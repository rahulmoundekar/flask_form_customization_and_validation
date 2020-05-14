from datetime import date
import phonenumbers
from flask_wtf import Form
from wtforms import ValidationError, StringField, validators, PasswordField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length


def validate_gender(form, field):
    if field.data == "-1":
        raise ValidationError("Sorry, you haven't chosen a Gender")


def validate_course(form, field):
    if field.data == "-1":
        raise ValidationError("Sorry, you haven't chosen a Course")


def validate_date_of_birth(form, field):
    today = date.today()
    age = today.year - form.date_of_birth.data.year - (
            (today.month, today.day) < (form.date_of_birth.data.month, form.date_of_birth.data.day))
    if not (20 < age < 30):
        raise ValidationError("You are no eligible for the Admission")


def validate_age(form, field):
    if form.age.data < 18:
        raise ValidationError("You must be at least 18 years old to Admit")


def validate_phone(form, mobile):
    try:
        p = phonenumbers.parse(form.mobile.data)
        if not phonenumbers.is_valid_number(p):
            raise ValueError()
    except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
        raise ValidationError('Phone number must be entered in the format: "+9999999999". Up to 10 digits allowed.')


class StudentForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=12)])
    email = StringField('Email', validators=[validators.DataRequired(), Email(message=('Not a valid email address.'))])

    mobile = StringField('Mobile', validators=[validators.DataRequired(), Length(max=10)])
    date_of_birth = DateField('Birthday', validators=[validators.DataRequired(), validate_date_of_birth])
    age = IntegerField('Age', validators=[validators.DataRequired(), validate_age])

    gender = SelectField('Gender', validators=[validators.DataRequired(), validate_gender],
                         choices=[('-1', '--Select--'),
                                  ('M', 'Male'),
                                  ('F', 'Female')])

    course = SelectField('Course', validators=[validators.DataRequired(), validate_course],
                         choices=[('-1', '--Select--'),
                                  ('Java', 'Java'),
                                  ('Python', 'Python')])

    # custom validation
