from django.shortcuts import render
from django.http import HttpResponse

from hello.models import Item,Timing

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "assistant.html",{"timings": Timing.objects.all()})
def items(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "items.html",{"items": Item.objects.all()})
    
def hello_world(request):
    return render(request, "hello_world.html", {"items": Item.objects.all()})

def sport(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "sport.html",{"items": Item.objects.all()})
def search(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "search.html")

def db(request):
    item = Item()
    item.save()

    items = Item.objects.all()

    return render(request, "db.html", {"items": items})

def update_db(request):
    id = request.GET['id']
    item = Item.objects.get(pk=id)
    item.availability = not item.availability
    item.save()
    return render(request, "assistant.html")
    

