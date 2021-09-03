from django.contrib.auth.models import User
from django.db import models


class Department(models.Model):
    """department"""
    name = models.CharField(max_length=500)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.name)


class Specialism(models.Model):
    """specialism"""
    name = models.CharField(max_length=500)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.name)


class Skills(models.Model):
    """soft_skills"""
    name = models.CharField(max_length=500)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.name)


class SoftSkill(models.Model):
    """soft_skills"""
    name = models.CharField(max_length=500)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.name)


class Language(models.Model):
    """english_level"""
    name = models.CharField(max_length=500)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.name)


class Level(models.Model):
    """Level"""
    level = models.IntegerField()
    description = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.name)
