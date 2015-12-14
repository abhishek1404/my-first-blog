from django.shortcuts import render
from .models import Post,Tag
from django.utils import timezone
from django.http import HttpResponse
from itertools import chain
import csv
from .forms import PostForm 
from django.shortcuts import redirect




# Create your views here.
def post_list(request):
	posts = Post.objects.all()
	
	posts = list(chain(posts))

	return render(request,'news/post_list.html',{'posts': posts})
	
def post_article(request):
	if 'name' in request.GET and request.GET['name']:
		q = request.GET['name']
		posts = Post.objects.filter(pk=q)
		
		return render(request, 'news/item.html',{'post': posts[0]})
	else:
		return HttpResponse('Please submit a search term.')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if  form.is_valid():
            post = form.save(commit=False)
            print "asasd======="
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('news.views.post_list')
    else:
        form = PostForm()
    return render(request, 'news/post_edit.html', {'form': form})