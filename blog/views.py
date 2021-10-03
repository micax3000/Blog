from django.shortcuts import render
from .models import Post

def home(request):
    contex = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', contex)
def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})
# Create your views here.
