
# Django
from django.db import models
from django.contrib.auth.models import User
from profiles.models import Country

# Create your models here.

# Empresa


class ProfileCompany(models.Model):
    """Perfil de la empresa"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    comercial_name = models.CharField(max_length=150,  blank=True, null=True)
    picture = models.ImageField(upload_to='Company/pictures', blank=True, null=True)
    phone_number = models.CharField(default=" ", max_length=20, blank=True, null=True)
    web_site = models.URLField(default=" ", blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    cedula = models.CharField(max_length=50, unique=True)
    biography = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.user.username