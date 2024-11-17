from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField, SelectField, IntegerRangeField, DecimalField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, FileAllowed, FileRequired, NumberRange
from werkzeug.utils import secure_filename

# Sign Up form
# logging into the website for the first time
# this is only for the customer, service_professional login is separate
class SignUpForm(FlaskForm):
    f_name = StringField('First name', validators=DataRequired())
    l_name = StringField('Last name', validators=DataRequired())
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    address = StringField('Address', validators=DataRequired())
    pincode = StringField('Pincode', validators=[DataRequired(), Length(min=6, max=6)])
    submit = SubmitField('Register')

    is_service_professional = BooleanField('Sign up as Service Professional')

    # might have to write a function that redirects to another form/page based on user selection
    # as of now, do not know where to include that
    # need to import redirect and url_for
    # will be writing the function for that, just in case 
    # def redirect service professional(self):
    # if self.is_service_professional.data:
    #     return redirect(url_for('service_professional_form'))
    # return None

# Sign up form - Service Professional
class SignUpFormSP(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    service_name = SelectField('Service you Provide', choices= ['Carpentry', 'Plumbing', 'Electrician', 'Cleaning'], validators=DataRequired()) #populate the choices more later on
    submit = SubmitField('Register')

# Sign up form for Service Professional leads to profile format

# Profile form for Service Professional
class ProfileSP(FlaskForm):
    experience = IntegerRangeField('Years of Experience', validators=[DataRequired()], default=0)
    price = DecimalField('Set Price for your Service', validators=[DataRequired()], places=2)
    services_provided = StringField('Sub services you provide', validators=DataRequired())
    upload_doc_verification = FileField('Upload File', validators=[FileRequired('File is required'), FileAllowed(['pdf'], 'Only pdfs allowed')])
    submit = SubmitField('Add to Profile')

# Login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


# Service Request Form
# To be accessed when the customer makes a service request
class ServiceRequestForm(FlaskForm):
    service_name = SelectField('Type of Service', validators=DataRequired()) # 'Carpentry', 'Plumbing', 'Electrician', 'Cleaning'
    submit = SubmitField('Request Service')

# Review Form 
# Feedback once service completed
class ReviewForm(FlaskForm):
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=1, max=5)])
    remarks = TextAreaField('Remarks', validators=[DataRequired()])
    submit = SubmitField('Submit Review')

# IDK if notification form is required but it is here commented
# class NotificationForm(FlaskForm):
#     is_read = BooleanField('Mark as Read')
#     submit = SubmitField('Yes')

# Admin Form 
# For the admin to create or update service names and service types
class ServiceTypeForm(FlaskForm):
    service_name = StringField('Name of Service', validators = [DataRequired()])
    description = TextAreaField('Service Description', validators=[DataRequired()])
    base_price = DecimalField('Base Price', validators=[DataRequired()], places=2)
    submit = SubmitField('Add Service')