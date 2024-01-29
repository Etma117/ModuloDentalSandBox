from django.urls import path
from .views import DentistaListView
urlpatterns = [
    path('ver-dentistas/', DentistaListView.as_view(), name='DentistaListView'),
]
