# Generated by Django 5.0.2 on 2024-03-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_doctorlist_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='Male', max_length=10),
        ),
    ]
