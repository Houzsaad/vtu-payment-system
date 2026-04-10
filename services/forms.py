from django import forms
from .models import ServiceCategory, ServicesPlan, ServiceProvider

class NetworkSelectionForm(forms.Form):
    network = forms.ModelChoiceField(
        queryset=ServiceProvider.objects.none(),
        empty_label='-- Select Network--',
        widget=forms.Select(attrs={'name': 'network'})
    )
    def __init__(self, *args, category_slug=None, **kwargs):
        super().__init__(*args, **kwargs)
        if category_slug:
            try:
                category = ServiceCategory.objects.get(slug=category_slug)
                self.fields['network'].queryset = ServiceProvider.objects.filter(
                category=category,
                is_active=True
            )
            except ServiceCategory.DoesNotExist:
                self.fields['network'].queryset = ServiceProvider.objects.none()
            
class AirtimeForm(forms.Form):
    phone = forms.CharField(
        max_length=11,
        min_length=11,
        widget=forms.TextInput(attrs={'inputmode': 'numeric', 'pattern': r'\d{11}', 'placeholder': 'Enter Phone Number'})
    )
    amount = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        min_value=50
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError('phone number must be digits only ')
        return phone

class DataPlanForm(forms.Form):
    plan = forms.ModelChoiceField(
        queryset=ServicesPlan.objects.none(),
        empty_label='-- Select Plan--'
    )
    phone = forms.CharField(
        max_length=11,
        min_length=11,
        widget=forms.TextInput(attrs={'inputmode': 'numeric', 'pattern': r'\d{11}', 'placeholder': 'Enter Phone Number'})
    )
    def __init__(self, network=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if network:
            self.fields['plan'].queryset = ServicesPlan.objects.filter(
                provider=network,
                is_active=True
            )
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError('phone number must be digits only ')
        return phone