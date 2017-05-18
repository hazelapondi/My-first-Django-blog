from django.shortcuts import render
#To add the line from .models import Post. 
#The dot before models means current directory/application. 
#Both views.py & models.py are in th same directory. 
#So we can use . and name of the file (without .py). 
#Then we import the name of the model ( Post)
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})	