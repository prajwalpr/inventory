from django import forms
from .models import Drinks

class DrinksForm(forms.ModelForm):
    class Meta:
        model = Drinks
        fields = [
            'name',
            'price',
            'units',
            'quantity',
        ]

        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control', "placeholder": 'Enter drinks name'}),
            'price': forms.NumberInput(),
        }



    def clean_name(self):
        return self.cleaned_data['name'].title()