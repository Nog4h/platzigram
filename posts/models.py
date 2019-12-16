#Post models

from django.db import models

class User(models.Model):
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=100)

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	bio = models.TextField(null=True)

	birthdate = models.DateField(blank=True, null=True)

	created = models.DateTimeField(auto_now_add=True)#va a cargar la fecha en la que se creó.
	modified = models.DateTimeField(auto_now=True)#va a guardar la fecha en la que se actualizó por última vez.