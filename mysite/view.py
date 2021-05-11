from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def removepunc(request):
    text=request.GET.get('text','default')
    print(text)
    return HttpResponse("REMOVEPUNC")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newline remove first")


def spaceremove(request):
    return HttpResponse("space remover back")

def charcount(request):
    return HttpResponse("charcount")



