from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()



class SignUpForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150, widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
            }))
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    
    nationality = forms.CharField(max_length=50, required=True, help_text='Required. Just tell us from where you are', widget=forms.TextInput(
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

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['password1']
            # self.cleaned_data['age'],
            # self.cleaned_data['gender'],
            # self.cleaned_data['nationality']
        )
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'age', 'gender', 'nationality')

class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)