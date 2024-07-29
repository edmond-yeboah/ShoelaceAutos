from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	gender = models.CharField(blank=True,null=True,max_length=5)
	phoneNumber = models.CharField(blank=True,null=True,max_length=10)
	address = models.CharField(blank=True, null=True,max_length=30)

	def __str__(self):
		return self.username
