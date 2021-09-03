from django.contrib import admin
from .models import Profile, UserSoftSkills, UserSkills, UserLanguages

# Register your models here.
admin.site.register(Profile)
admin.site.register(UserSkills)
admin.site.register(UserSoftSkills)
admin.site.register(UserLanguages)