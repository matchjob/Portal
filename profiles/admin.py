from django.contrib import admin
from .models import Department, Specialism, Skills, SoftSkill, Language, Level, Country
# Register your models here.

admin.site.register(Department)
admin.site.register(Specialism)
admin.site.register(Skills)
admin.site.register(SoftSkill)
admin.site.register(Language)
admin.site.register(Level)
admin.site.register(Country)