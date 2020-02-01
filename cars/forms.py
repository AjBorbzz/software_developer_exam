from django.forms import ModelForm
from .models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['car_brand', 'car_model', 'car_owner','car_color']
