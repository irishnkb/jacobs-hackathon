from django.shortcuts import render
from django.http import HttpResponse

from .models import Item

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "assistant.html")

def hello_world(request):
    return render(request, "hello_world.html")


def db(request):

    greeting = Item()
    greeting.save()

    greetings = Item.objects.all()

    return render(request, "db.html", {"items": greetings})
