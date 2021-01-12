from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/event_reg', views.event_reg, name = 'event_reg'),
    path('/part_reg', views.part_reg, name = 'part_reg'),
    path('/event_dash', views.event_dash, name = 'event_dash'),
    ]