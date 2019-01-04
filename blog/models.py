from django.db import models
from .validators import email_validators

# Create your models here.

class Contact(models.Model):
    name = models.CharField(
        max_length=100,
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
        validators=[email_validators],
        error_messages={
            'unique': 'Email already exists.Please enter another email',
        },
    )
    phone = models.IntegerField()
    comment = models.TextField()

    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact'
        verbose_name_plural = "Contacts"
