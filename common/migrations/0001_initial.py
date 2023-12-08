# Generated by Django 4.2.8 on 2023-12-08 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Nomi')),
                ('image', models.ImageField(upload_to='about/', verbose_name='Rasm')),
                ('description', models.TextField(verbose_name='Izoh')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name="To'liq ismi")),
                ('image', models.ImageField(upload_to='team/')),
                ('position', models.CharField(max_length=50, verbose_name='Lavozim')),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Nome')),
                ('icon', models.CharField(max_length=50, verbose_name='Icon')),
                ('description', models.TextField(verbose_name='Izoh')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('status', models.ManyToManyField(to='common.status', verbose_name='Kategoriyalar')),
            ],
        ),
    ]