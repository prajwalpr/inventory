from django.core import validators

class PhoneValidators(validators.RegexValidator):
    regex = r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$'
    message = 'Enter a valid phone number.'

class NameValidators(validators.RegexValidator):
    regex = r'^(\s)*[A-Za-z]+((\s)?((\'|\-|\.)?([A-Za-z])+))*(\s)*$'
    message = 'Enter a valid name.'

class TextValidators(validators.RegexValidator):
    regex = r'^[a-zA-Z ]*$'
    message = 'Enter valid text.'