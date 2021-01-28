from django.shortcuts import render
from .models import *
from random import randint
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def random_number():
    return randint(10**4, 10**5 - 1)

def email_host(post):
    subject = "Thank You for registering with us"
    message = "Event ID: " + str(post.event_id) + "\nEvent name: " + str(post.event_name) + "\nDescription: " + str(post.description) + "\nRegistration starts from: " + str(post.from_date) + " " + str(post.from_time) + "\nDeadline: " + str(post.to_date) + " " + str(post.to_time) + "\nPoster link: " + str(post.poster_link)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [post.host_id]
    send_mail(subject, message, email_from, recipient_list)

def email_part(post):
    subject = "Thank You for participating"
    if post.people != None:
        message = "Participant ID: " + str(post.part_id) + "\nParticipant name: " + str(post.part_name) + "\nContact Number: " + str(post.contact) + "\nEvent: " + str(post.event) + "\nType: Group" + "\nNumber of participants: " + str(post.people)
    else:
        message = "Participant ID: " + str(post.part_id) + "\nParticipant name: " + str(post.part_name) + "\nContact Number: " + str(post.contact) + "\nEvent: " + str(post.event) + "\nType: Individual" 
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [post.email_id]
    send_mail(subject, message, email_from, recipient_list)

def event_reg(request):
    if request.method == 'POST':
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
        email_host(post)
        return render(request, 'Event Registration.html')
    else :
        return render(request, 'Event Registration.html')

def part_reg(request):
    if request.method == 'POST':
        post = participant()
        post.part_id = random_number()
        post.part_name = request.POST.get('part_name')
        post.contact = request.POST.get('contact')
        post.email_id = request.POST.get('email_id')
        post.event = request.POST.get('event_name')
        post.reg_type = request.POST.get('type')
        post.people = request.POST.get('people')
        post.save()   
        email_part(post)
        return render(request, 'Participant Registration.html')
    else :
        return render(request, 'Participant Registration.html')

def event_dash(request):
    return render(request, 'Event Dashboard.html')