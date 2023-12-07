from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author' : 'Sahan',
        'title' : 'Blog Post 1',
        'content' : 'First post Content',
        'date_posted' : 'December 7,2023'
    },
    {
        'author' : 'Sara',
        'title' : 'Blog Post 2',
        'content' : 'Second post Content',
        'date_posted' : 'December 7,2023'
    }

]


def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    context = {
        'posts' : posts
    }
    return render(request , 'blog/home.html', context)

def log(request):
    # return HttpResponse('<h1>This is log</h1><p>lorem</p>')
    return render(request , 'blog/about.html' , {'title' : 'about'})

    