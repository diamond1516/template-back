from django.db import models
# Create your models here.


class Workflow(models.Model):
    title = models.CharField(max_length=50, verbose_name='Nome')
    icon = models.CharField(max_length=50, verbose_name='Icon')
    description = models.TextField(verbose_name='Izoh')


class About(models.Model):
    title = models.CharField(max_length=50, verbose_name='Nomi')
    image = models.ImageField(upload_to='about/', verbose_name='Rasm')
    description = models.TextField(verbose_name='Izoh')


class Team(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="To'liq ismi")
    image = models.ImageField(upload_to='team/')
    position = models.CharField(max_length=50, verbose_name='Lavozim')


class Status(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.status


class Portfolio(models.Model):
    title = models.CharField(max_length=255, verbose_name='Nomi', null=True)
    status = models.ManyToManyField(
        Status,
        verbose_name='Kategoriyalar'
    )
    image = models.ImageField(upload_to='portfolio/')
