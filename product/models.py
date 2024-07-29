from django.db import models

# Create your models here.

class Car(models.Model):
	brand= models.CharField(blank=True,null=True,max_length=30)
	model = models.CharField(blank=True,null=True,max_length=30)
	year = models.CharField(blank=True,null=True,max_length=30)
	color = models.CharField(blank=True,null=True,max_length=30)

	def __str__(self):
		return self.brand