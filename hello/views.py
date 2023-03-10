from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import random
from . import fortuneList

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def home(request):

    fortune = random.choice(fortuneList.fortuneList)
    context = {'fortune': fortune}
    return render(request, "home.html", context)
