# Generated by Django 4.2.8 on 2023-12-08 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='Nomi'),
        ),
    ]
