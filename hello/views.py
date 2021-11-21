from django.shortcuts import render
from django.http import HttpResponse

from .models import Item

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "assistant.html")

def hello_world(request):
    return render(request, "hello_world.html", {
        'items': Item.objects.all(),
    })

def db(request):
    item = Item()
    item.save()

    items = Item.objects.all()

    return render(request, "db.html", {"items": items})

def update_db(request):
    print(request.GET)
    id = request.GET['id']
    print(id)
    item = Item.objects.get(pk=id)
    print("availablity = ", item.availability)
    item.availability = not item.availability
    print("availablity = ", item.availability)
    item.save()
    return render(request, "assistant.html")
    

