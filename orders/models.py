from django.db import models

class Order(models.Model):
	name = models.CharField(max_length=50)
	item = models.CharField(max_length=50)
	quantity = models.IntegerField()
	price = models.IntegerField()

	def __str__(self):
		return self.name