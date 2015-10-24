from django.db import models

# Create your models here.
from django.utils import timezone
class Post(models.Model):
	author=models.TextField(default='auth.User')
	type_p=models.TextField(default='')
	title=models.CharField(max_length=200)
	description=models.TextField(default='')
	tags = models.TextField(default='')
	country = models.TextField(default='')
	language = models.TextField(default='')
	video=models.TextField(default='')
	release_date=models.TextField(default='')
	Published_Date=models.DateTimeField(blank=True,null=True)


	def publish(self):
		self.Published_Date=timezone.now()
		self.save()

	def __str__(self):
		return self.title
class Text_Post(models.Model):
	author=models.TextField(default='auth.User')
	type_p=models.TextField(default='')
	title=models.CharField(max_length=200)
	description=models.TextField(default='')
	tags = models.TextField(default='')
	country = models.TextField(default='')
	language = models.TextField(default='')
	image = models.TextField(default='')
	content=models.TextField(default='')
	release_date=models.TextField(default='')
	Published_Date=models.DateTimeField(blank=True,null=True)


	def publish(self):
		self.Published_Date=timezone.now()
		self.save()

	def __str__(self):
		return self.title

