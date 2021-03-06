# Generated by Django 3.2.6 on 2021-09-08 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_delete_profilecompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='academic_title',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, default=' ', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='web_site',
            field=models.URLField(blank=True, default=' ', null=True),
        ),
    ]
