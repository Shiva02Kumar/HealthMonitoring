# Generated by Django 5.0.2 on 2024-02-28 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_doctorlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorlist',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]