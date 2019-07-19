from django import forms
from .models import Pki, Part


class PkiForm(forms.ModelForm):
    class Meta:
        model = Pki
        fields = ('name_type', 'part_name', 'name', 'serial_number', 'country')


class PartForm(forms.Form):
    CHOICES = Part.objects.all().values_list('id', 'part_name')
    select = forms.ChoiceField(choices=CHOICES, label='',
                               widget=forms.Select(attrs={
                                'class': 'custom-select',
                                'onchange': 'this.form.submit()'}))
