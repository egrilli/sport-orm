from django.urls import path
from . import views

urlpatterns = [
	path('orm1', views.index, name="index"),
	path('orm2', views.index1, name="index1"),
	path('initialize', views.make_data, name="make_data"),
]
