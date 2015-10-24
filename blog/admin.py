from django.contrib import admin

# Register your models here.
from .models import Post,Text_Post
admin.site.register(Post)
admin.site.register(Text_Post)