

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Customer




class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', max_length=100, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    username = forms.CharField(max_length=30, label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password' })
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'})
        self.fields['password2'].label = 'Confirmation Password'
        self.fields['password2'].help_text = '<span class="form-text text-muted">Enter the same password as before, for verification.</span>'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'address', 'city', 'zipcode']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
        }