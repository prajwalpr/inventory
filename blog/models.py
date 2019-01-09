from django.db import models
from .validators import PhoneValidators, NameValidators, TextValidators

# Create your models here.

class Contact(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[NameValidators()],
    )
    email = models.EmailField(
        unique=True,
    )
    phone = models.CharField(
        max_length=30,
        validators=[PhoneValidators()],
        )
    comment = models.TextField(
        validators=[TextValidators()],
    )

    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact'
        verbose_name_plural = "Contacts"


    def __str__(self):
        pass