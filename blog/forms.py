from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'phone',
            'comment'
        ]
        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control', "placeholder": 'Name'}),
            'email': forms.TextInput(attrs={"class": 'form-control', "placeholder": 'Email'}),
            'phone': forms.TextInput(attrs={"class": 'form-control', "placeholder": 'Phone'}),
            'comment': forms.Textarea(attrs={"class": 'form-control', "placeholder": 'Comment', 'rows': 5})
        }
