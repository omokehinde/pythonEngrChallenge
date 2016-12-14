from django.db import models


class NameNEmail(models.Model):
	name = models.CharField(max_length=250)
	email = models.EmailField(max_length=150)

	# This method makes the terminal to print out the name and email 
	# whenever you query the db from the terminal usinb NameNEmail.objects.all()
	def __str__(self):
		return self.name + ', ' + self.email