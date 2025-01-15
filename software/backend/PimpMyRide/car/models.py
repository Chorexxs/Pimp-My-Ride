from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()


class Sensor(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)


class Light(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    is_on = models.BooleanField(default=False)
