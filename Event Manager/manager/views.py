from django.shortcuts import render
from .models import *
from random import randint
from django.core.mail import send_mail
from django.conf import settings
from datetime import date

def index(request):
    return render(request, 'index.html')

def random_number():
    return randint(10**4, 10**5 - 1)

def email_host(post):
    subject = "Thank You for registering with us"
    message = "Event ID: " + str(post.event_ID) + "\nEvent name: " + str(post.event_name) + "\nDescription: " + str(post.description) + "\nFrom: " + str(post.from_date) + " " + str(post.from_time) + "\nTo: " + str(post.to_date) + " " + str(post.to_time) + "\nDeadline: " + str(post.registration_deadline) + "\nPoster link: " + str(post.poster_link)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [post.email_ID]
    send_mail(subject, message, email_from, recipient_list)

def email_part(post):
    subject = "Thank You for participating"
    if post.registration_type == "Group":
        message = "Participant ID: " + str(post.particpant_ID) + "\nParticipant name: " + str(post.name) + "\nContact Number: " + str(post.contact) + "\nEvent: " + str(post.event) + "\nType: Group" + "\nNumber of participants: " + str(post.number_of_participants)
    else:
        message = "Participant ID: " + str(post.particpant_ID) + "\nParticipant name: " + str(post.name) + "\nContact Number: " + str(post.contact) + "\nEvent: " + str(post.event) + "\nType: Individual" 
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [post.email_ID]
    send_mail(subject, message, email_from, recipient_list)

def event_reg(request):
    if request.method == 'POST':
        post = event()
        post.event_ID = random_number()
        post.event_name = request.POST.get('event_name')
        post.description = request.POST.get('description')
        post.from_date = request.POST.get('from_date')
        post.from_time = request.POST.get('from_time')
        post.to_date = request.POST.get('to_date')
        post.to_time = request.POST.get('to_time')
        post.registration_deadline = request.POST.get('deadline')
        post.poster_link = request.POST.get('poster_link')
        post.email_ID = request.POST.get('host_id')
        post.password = request.POST.get('password')
        post.save()   
        email_host(post)
        return render(request, 'Event Registration.html')
    else :
        return render(request, 'Event Registration.html')

def part_reg(request):
    x = event.objects.all()
    t = date.today()  
    events = []
    for i in x:    
        if i.registration_deadline >= t:
            events.append(i.event_name) 
    if request.method == 'POST':
        post = participant()
        post.particpant_ID = random_number()
        post.name = request.POST.get('part_name')
        post.contact = request.POST.get('contact')
        post.email_ID = request.POST.get('email_id')
        post.event_name = request.POST.get('event')
        post.registration_type = request.POST.get('type')
        post.number_of_participants = request.POST.get('people')
        post.save()   
        email_part(post)
        return render(request, 'Participant Registration.html', {'events': events})
    else :
        return render(request, 'Participant Registration.html', {'events': events})

def event_dash(request):
    return render(request, 'Event Dashboard.html')