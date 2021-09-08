"""User forms."""

# Django
from django import forms
from profiles.models import Language, Department, Specialism, Skills, SoftSkill, Level, Country
from users.models import Profile


class ProfileForm(forms.Form):
    """Profile form."""

    department = forms. ModelChoiceField(queryset=Department.objects.values().filter(), label='departament' )
    specialism = forms.ModelChoiceField(queryset=Specialism.objects.values().filter(), label='specialism')
    currently_working = forms.BooleanField(required=False)
    search_job = forms.BooleanField(required=False)
    home_office = forms.BooleanField(required=False)
    freelancer = forms.BooleanField(required=False)
    residence_change = forms.BooleanField(required=False)
    remote_work = forms.BooleanField(required=False)
    to_travel = forms.BooleanField(required=False)
    desired_salary = forms.IntegerField(required=False)
    current_salary = forms.IntegerField(required=False)
    picture = forms.ImageField(required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    web_site = forms.URLField(required=False)
    lat = forms.FloatField(required=False)
    lon = forms.FloatField(required=False)
    biography = forms.CharField(max_length=500, required=False)
    country = forms.ModelChoiceField(queryset=Country.objects.values().filter(), label='country')
    nearby_search = forms.BooleanField(required=False)
    gender = forms.CharField(max_length=50, required=False)
    academic_title = forms.CharField(max_length=50, required=False)

