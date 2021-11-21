from django.shortcuts import render
from django.http import HttpResponse

from hello.models import Item,Timing

from datetime import date
from datetime import datetime

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    timing = 0

    for t in Timing.objects.all():
        if t.date == date.today():
            timing = t
    if (str(datetime.now()).split(':')[0][11:13] - t[0].date.opening_time.split(':')[0]) > (str(datetime.now()).split(':')[0][11:13] - t[1].date.opening_time.split(':')[0]):
        timing = t[1]
    else:
        timing = t[0]

    return render(request, "assistant.html",{"timing": timing})

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

def board(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "board.html")
    
def everyday(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "everyday.html")

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
