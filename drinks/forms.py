from django import forms

from category.models import Category
# from units.models import Units
from .models import Drinks


class DrinksForm(forms.ModelForm):
    # category = forms.ModelChoiceField(
    #     queryset=Category.objects.all(),
    #     empty_label="Choice",
    #     widget=forms.Select(attrs={"class": "form-control"})
    # )

    class Meta:
        model = Drinks
        fields = [
            'name',
            'price',
            'units',
            'quantity',
            'image',
            # 'category',
        ]

        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control', "placeholder": 'Enter drinks name'}),
            'price': forms.NumberInput(attrs={"class": 'form-control'}),
            'units': forms.Select(attrs={"class": "form-control"}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'image': forms.FileInput(),
        }

    def clean_name(self):
        return self.cleaned_data['name'].title()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['units'].empty_label = "Choose"


    def save(self, commit=True):
        drinks = super(DrinksForm, self).save(commit=False)
        if commit:
            drinks.save()
        return drinks