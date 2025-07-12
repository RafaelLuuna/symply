from django import forms
from django.core.exceptions import ValidationError
from . import models

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class CadastroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['confirm_password'] = forms.CharField(max_length="100",widget=forms.PasswordInput())
        # self.fields['username'].help_text = None

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']

        if confirm_password and password and confirm_password != password:
            self.add_error('confirm_password',"Password doesn't match")


    class Meta:
        model = models.CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
            "password"
        ]

        widgets = {
            'password': forms.PasswordInput(),
        }

        labels = {
            'username': 'Usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
            'role': 'Tipo de usuário',
            'password': 'Senha',
        }
    

        
        

