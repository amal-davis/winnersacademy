# Generated by Django 4.2.5 on 2024-01-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winnerapp', '0007_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='course',
            name='heading',
            field=models.CharField(default='', max_length=255),
        ),
    ]
