from .models import Units

from django import forms

class UnitForm(forms.ModelForm):
    name = forms.CharField(
        label = 'Name',
        widget = forms.TextInput(attrs={'class':'from-control', 'placeholder':'Litre'})
    )

    print_name = forms.CharField(
        label = 'Print Name',
        widget = forms.TextInput(attrs={'class':'from-control', 'placeholder':'Ltr'})
    )

    class Meta:
        model = Units
        fields = {'name', 'print_name'}


    def __init__(self, *args , **kwargs):
        super(UnitForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        return self.cleaned_data['name'].title()
