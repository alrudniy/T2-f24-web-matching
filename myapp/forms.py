from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

#class CreateUserForm(UserCreationForm):
#    class Meta:
#        model = User
#        fields = ['username', 'firstname', 'lastname', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your username',
    }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password',
    }))

class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=150)
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

class PropertyForm(forms.Form):
    name = forms.CharField(max_length=255)
    size_sqft = forms.IntegerField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = forms.IntegerField()
    bathrooms = forms.IntegerField()
    street_address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    image = forms.ImageField(required=False) # Image field
