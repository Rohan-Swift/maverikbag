from django.db import models


# Create your models here.
class Counting(models.Model):
    volunteer = models.IntegerField()
    event = models.IntegerField()


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    instagram = models.URLField()
    img = models.ImageField(upload_to='volunteer_image')


class Pay(models.Model):
    img = models.ImageField(upload_to='qr_code')


class Email(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)


class Image(models.Model):
    img = models.ImageField()


class TeamPic(models.Model):
    img = models.ImageField()
