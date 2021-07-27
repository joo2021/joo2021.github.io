from django.shortcuts import render
from .models import Blog
from django.utils import timezone
# Create your views here.



def first(request):
    return render(request, 'first.html')

def index(request):
    return render(request, 'index.html')
    
def party(request):
    return render(request, 'party.html')

def about(request):
    return render(request, 'about.html')

def cel(request):
    return render(request, 'cel.html')

def food(request):
    return render(request, 'food.html')

def letter(request):  
    blogs = Blog.objects
    return render(request, 'letter.html', {'blogs': blogs})


def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return render(request, 'index.html')