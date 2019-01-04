from django.db import models

# Create your models here.

class Units(models.Model):
    name = models.CharField(max_length=50, unique= True)
    print_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

     # this is necessary to create select box
    def __str__(self):
        return self.print_name

    class Meta:
        db_table = 'units'
        ordering = ["print_name"]  # this is used to add name in select box
