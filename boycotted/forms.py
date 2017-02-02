from django import forms
from boycotted.models import Boycott, Boycotted


class BoycottedForm(forms.ModelForm):
    class Meta:
        model = Boycotted
        fields = ['name', 'zip']

class BoycottForm(forms.ModelForm):
    class Meta:
        model = Boycott
        fields = ['reason']

