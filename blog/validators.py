
import re

from django.core.exceptions import ValidationError


def email_validators(value):
    regex = '^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'
    pattern = re.compile(regex)
    if not pattern.match(value):
        raise ValidationError("Email is not valid")
