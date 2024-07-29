from django.urls import path
from authentication import views




urlpatterns = [
	path("register/",views.register),
	path("login/",views.login),
	path("logout/",views.logout)
]
