from django.shortcuts import render
from .models import *
from random import randint

def index(request):
    return render(request, 'index.html')

def random_number():
    return randint(10**4, 10**5 - 1)

def event_reg(request):
    if request.method == 'POST':
            if request.POST.get('event_name'):
                post = register()
                post.event_id = random_number()
                post.event_name = request.POST.get('event_name')
                post.description = request.POST.get('description')
                post.from_date = request.POST.get('from_date')
                post.from_time = request.POST.get('from_time')
                post.to_date = request.POST.get('to_date')
                post.to_time = request.POST.get('to_time')
                post.poster_link = request.POST.get('poster_link')
                post.host_id = request.POST.get('host_id')
                post.save()          
                return render(request, 'Event Registration.html')
    else :
        return render(request, 'Event Registration.html')

def part_reg(request):
    return render(request, 'Participant Registration.html')

def event_dash(request):
    return render(request, 'Event Dashboard.html')