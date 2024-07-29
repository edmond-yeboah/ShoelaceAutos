from django.urls import path
from product import views
urlpatterns = [
	path("addCar/",views.addCar),
	path("getCars/",views.getCar)
]
