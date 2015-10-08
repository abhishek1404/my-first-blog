from django.db import models

# Create your models here.
from django.utils import timezone
class Post(models.Model):
	author=models.ForeignKey('auth.User')
	title=models.CharField(max_length=200)
	text=models.TextField()
	Created_date=models.DateTimeField(default=timezone.now)
	Published_Date=models.DateTimeField(blank=True,null=True)


	def publish(self):
		self.Published_Date=timezone.now()
		self.save()

	def __str__(self):
		return self.title