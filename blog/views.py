from django.shortcuts import render
from .models import Post,Text_Post
from django.utils import timezone
from django.http import HttpResponse
from itertools import chain


# Create your views here.
def post_list(request):
	posts = Post.objects.all()
	text_post = Text_Post.objects.all()
	posts = list(chain(posts,text_post))

	return render(request,'blog/post_list.html',{'posts': posts})

def search_form(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		posts = Post.objects.filter(title__contains=q)
		text_post = Text_Post.objects.filter(title__contains=q)
		posts = list(chain(posts,text_post))

		return render(request, 'blog/search_results.html',{'posts': posts})
	else:
		return HttpResponse('Please submit a search term.')

def video_page(request):
	if 'name' in request.GET and request.GET['name']:
		q = request.GET['name']
		posts = Post.objects.filter(title__contains=q)
		
		return render(request, 'blog/item.html',{'posts': posts})
	else:
		return HttpResponse('Please submit a search term.')
def text_page(request):
	if 'name' in request.GET and request.GET['name']:
		q = request.GET['name']
		
		posts = Text_Post.objects.filter(title__contains=q)
		
		return render(request, 'blog/item.html',{'posts': posts})
	else:
		return HttpResponse('Please submit a search term.')


#Author	type_p	title	description	tags	country	language	video	videorelease_date	Published-Date

