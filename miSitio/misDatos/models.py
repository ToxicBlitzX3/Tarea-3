from django.db import models

# Create your models here.
class MisDatos(models.Model):
	nombre = models.CharField(max_length=30)
	skills = models.TextField()
	telefono = models.IntegerField()
	email = models.EmailField()
	imagen = models.FileField()
#class Social(models.Model):
	facebook = models.CharField(max_length=30)
	youtube = models.CharField(max_length=30)
	twitter = models.CharField(max_length=30)

	def __unicode__(self):
		#return self.nombre
 		return '%s %s %s %s' % (self.nombre, self.skills, self.telefono, self.email)
 		#https://swea.googlecode.com/svn-history/r9/trunk/project/models.py