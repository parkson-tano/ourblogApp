from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")


def blogpost(request):
    return render(request, 'index.html' ,{'name': 'blogpost'})