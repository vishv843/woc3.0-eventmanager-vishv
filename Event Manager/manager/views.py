from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, 'index.html')

def event_reg(request):
    return render(request, 'Event Registration.html')

def part_reg(request):
    return render(request, 'Participant Registration.html')

def event_dash(request):
    return render(request, 'Event Dashboard.html')