from django import forms

from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
            'image',
        ]
        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control', "placeholder": 'Enter category name'})
            }


    def __init__(self, *args , **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        return self.cleaned_data['name'].title()


    def save(self, commit=True):
        category = super(CategoryForm, self).save(commit=False)
        if commit:
            category.save()
        return category
