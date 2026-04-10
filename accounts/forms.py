from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Costomer

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Costomer
        fields = ['phone_number', 'email', 'password', 'transaction_pin']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords isn't matched")
        return cleaned_data
        
class PinForm(forms.Form):
    pin = forms.CharField(
        max_length=128,
        #min_digits=4,
        widget=forms.PasswordInput()
    )
        
    def clean_pin(self):
        pin = self.cleaned_data.get("pin")
        digits = pin
        if not pin.isdigits:
            raise forms.ValidationError("PIN must contain only number")

        return pin

