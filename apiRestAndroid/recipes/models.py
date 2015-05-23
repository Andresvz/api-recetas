#encoding:utf-8
from django.db import models

class Recipe(models.Model):
	name = models.CharField(max_length=50)
	ingredients = models.TextField()
	recipe_type = models.CharField(max_length=50)
	time = models.CharField(max_length=50)
	chef_name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name