from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
	"an Article pusted on by any user"
	title = models.TextField(blank=True)
	author = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField('Tag', related_name='tag_posts', blank=True,null=True)
	content = models.TextField(blank=True)
	def __str__(self):
		return self.title
    


class Tag(models.Model):
    """
    Defines a keyword categorisation for posts
    """
    name = models.CharField(max_length=50)    

    def __unicode__(self):
        return self.name

    