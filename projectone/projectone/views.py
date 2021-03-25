from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from tution.models import Contact


def home(request):
    name = ['Rajib', 'Anik', 'Tama', 'Annana', 'Juthi']
    context = {'name': name}
    return render(request, 'home.html', context)
