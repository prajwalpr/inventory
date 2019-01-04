from django.core import validators


class UsernameValidator(validators.RegexValidator):
    regex = r'^[\w.-]+$'
    message = 'Enter a valid username. This value may contain only letters, numbers, and ./-/_ characters.'

class EmailValidator(validators.RegexValidator):
    regex = r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'
    message = 'Enter a valid email.This value may contain only letters, numbers, and ./-/_ characters.'


class ContactValidator(validators.RegexValidator):
    regex = r'((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}'
    message = 'Please enter valid number.'
