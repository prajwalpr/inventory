from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(default='default.png')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
        verbose_name = 'Category'
        verbose_name_plural = "Categories"



