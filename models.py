from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings



class Product(models.Model):

   name = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   total = models.IntegerField()
   quantity = models.IntegerField()

   class Meta:
      db_table = "Product"



class Cart(models.Model):
	
	Username = models.CharField(max_length = 50)
	Product = models. CharField(max_length = 50)
	Price = models.IntegerField()
	quantity = models.IntegerField()

	class Meta:
		db_table = "Cart"

	

	
	
