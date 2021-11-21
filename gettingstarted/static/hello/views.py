from django.shortcuts import render
from django.http import HttpResponse

from .models import Item
from .models import Timmings

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "assistant.html",{"timmings": Timmings.objects.all()})

def items(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "items.html")
    
def hello_world(request):
    return render(request, "hello_world.html", {"items": Item.objects.all()})

def sport(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "sport.html",{"items": Item.objects.all()})

def update_db(request):
    id = request.GET['id']
    item = Item.objects.get(pk=id)
    item.availability = not item.availability
    item.save()
    return render(request, "assistant.html")
    

