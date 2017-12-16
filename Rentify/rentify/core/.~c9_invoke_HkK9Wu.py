from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class SignUpForm(UserCreationForm):
    
    email = forms.Field(widget=forms.EmailInput(attrs={'class':'form-control'}))
            attrs={
                'placeholder': 'Nationality',
            }))
    age = forms.IntegerField(required=False, help_text='Optional.', widget=forms.TextInput(
            attrs={
                'placeholder': 'Age',
            }))
    
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = forms.ChoiceField(choices=GENDER, required=True)
    # profile = forms.ImageField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'age', 'gender', 'nationality')

class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)