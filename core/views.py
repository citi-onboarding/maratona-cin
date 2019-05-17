from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

def index(request):
    return render(request, 'index.html', {'posts':Post.objects.all()})