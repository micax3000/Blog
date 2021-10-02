from django.shortcuts import render

posts = [
    {
        'author': 'Micax',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 1, 2021'
    },
    {
        'author': 'Maja',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 1, 2021'
    }

]
def home(request):
    contex = {
        'posts': posts
    }
    return render(request, 'blog/home.html', contex)
def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})
# Create your views here.
def login(request):
    return render(request, 'blog/login.html',{'title': 'Login'})