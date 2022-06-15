from django import forms


class FormContacto(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    message = forms.CharField(required=True)