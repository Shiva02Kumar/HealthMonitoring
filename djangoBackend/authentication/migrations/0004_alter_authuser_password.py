# Generated by Django 5.0.2 on 2024-02-24 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_authuser_age_authuser_email_authuser_fullname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='password',
            field=models.CharField(default='', max_length=12),
        ),
    ]
