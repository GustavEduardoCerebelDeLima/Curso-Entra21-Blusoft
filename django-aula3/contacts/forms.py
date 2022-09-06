from .models import *
from django import forms


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name', 'nickname', 'cel', 'mail', 'register_date', 'description', 'categories'
        ]
        