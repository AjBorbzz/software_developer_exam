from django.db import models


class Car(models.Model):

    class Meta:
        ordering = ['order']

    RED = 'Red'
    BLUE = 'Blue'
    COLOR = [(RED, 'Red'), (BLUE, 'Blue')]
    car_brand = models.CharField(max_length=200)
    car_model = models.CharField(max_length=50)
    car_owner = models.CharField(max_length=200)
    car_color = models.CharField(
        max_length=8, choices=COLOR)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.car_model

