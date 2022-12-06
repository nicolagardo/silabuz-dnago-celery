from django import forms

class InputFom(forms.Form):
    name = forms.CharField(max_length = 3, empty_value="Nombre")
    email = forms.EmailField()

    