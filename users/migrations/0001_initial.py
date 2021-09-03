# Generated by Django 3.2.6 on 2021-08-27 03:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currently_working', models.BooleanField()),
                ('search_job', models.BooleanField()),
                ('home_office', models.BooleanField()),
                ('freelancer', models.BooleanField()),
                ('residence_change', models.BooleanField()),
                ('remote_work', models.BooleanField()),
                ('to_travel', models.BooleanField()),
                ('desired_salary', models.IntegerField()),
                ('current_salary', models.IntegerField()),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('phone_numbre', models.CharField(blank=True, max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='profiles.department')),
            ],
        ),
        migrations.CreateModel(
            name='UserSoftSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('SoftSkill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.softskill')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.level')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='UserSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.level')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.skills')),
            ],
        ),
        migrations.CreateModel(
            name='UserLanguages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.language')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.level')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='languages',
            field=models.ManyToManyField(through='users.UserLanguages', to='profiles.Language'),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(through='users.UserSkills', to='profiles.Skills'),
        ),
        migrations.AddField(
            model_name='profile',
            name='soft_skills',
            field=models.ManyToManyField(through='users.UserSoftSkills', to='profiles.SoftSkill'),
        ),
        migrations.AddField(
            model_name='profile',
            name='specialism',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='profiles.specialism'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
