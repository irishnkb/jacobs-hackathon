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
