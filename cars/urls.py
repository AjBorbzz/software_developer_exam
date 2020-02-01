from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('instructions', views.instructions, name='instructions'),
    path('enroll', views.enroll, name='enroll'),
]