from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(UserSkills)
admin.site.register(UserSoftSkills)
admin.site.register(UserLanguages)