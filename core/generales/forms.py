# forms.py

from django import forms

class UserRecoveryForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=150)
