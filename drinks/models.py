from django.db import models

from category.models import Category
from units.models import Units


class Drinks(models.Model):
    cid = models.ForeignKey(Category, related_name="drinks", on_delete=models.CASCADE)
    units = models.ForeignKey(Units, related_name="drinks", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    name = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'drinks'
        ordering = ['name']
            
