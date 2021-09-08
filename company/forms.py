"""User forms."""

# Django
from django import forms


class CompanyProfileForm(forms.Form):
    """Profile form."""

    picture = forms.ImageField(required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    web_site = forms.URLField(required=False)
    lat = forms.FloatField(required=False)
    lon = forms.FloatField(required=False)
    biography = forms.CharField(max_length=500, required=False)



