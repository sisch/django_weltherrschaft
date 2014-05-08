from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Entry(models.Model):
	"""Ein Eintrag im Weltherrschaftsblog
	"""
	
	title = models.CharField(max_length=100)
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	color = models.CharField(max_length=7)

