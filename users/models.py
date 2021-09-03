from django.contrib.auth.models import User
from django.db import models
from profiles.models import Language, Department, Specialism, Skills, SoftSkill, Level


class Profile(models.Model):
    """profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    specialism = models.ForeignKey(Specialism, on_delete=models.DO_NOTHING)
    skills = models.ManyToManyField(Skills, through='UserSkills')
    soft_skills = models.ManyToManyField(SoftSkill, through='UserSoftSkills')
    languages = models.ManyToManyField(Language, through='UserLanguages')
    currently_working = models.BooleanField()
    search_job = models.BooleanField()
    home_office = models.BooleanField()
    freelancer = models.BooleanField()
    residence_change = models.BooleanField()
    remote_work = models.BooleanField()
    to_travel = models.BooleanField()
    desired_salary = models.IntegerField()
    current_salary = models.IntegerField()
    picture = models.ImageField(blank=True)
    phone_numbre = models.CharField(max_length=20, blank=True)
    web_site = models.URLField()
    lat = models.FloatField()
    lon = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.user.username


class UserSkills(models.Model):
    """UserSkills"""
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s : %s - %s' % (self.profile.user.username, self.skill.name, self.level.name)


class UserSoftSkills(models.Model):
    """UserSoftSkills"""
    SoftSkill = models.ForeignKey(SoftSkill, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s : %s - %s' % (self.profile.user.username, self.SoftSkill.name, self.level.name)


class UserLanguages(models.Model):
    """UserSoftSkills"""
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s : %s - %s' % (self.profile.user.username, self.language.name, self.level.name)

