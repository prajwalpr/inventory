import json

from django.contrib import messages
from django.shortcuts import render, redirect
# from .models import Blog
#from .forms import BlogForm, ContactForm
from .forms import ContactForm
from django.core import serializers
from django.http import HttpResponse, JsonResponse


# Create your views here.

def home(request):
    context = {}
    form_contact = ContactForm(request.POST or None)
    if request.method == "POST":
        if form_contact.is_valid():
            form_contact.save()
            return redirect('blog:contact')
    context['contact_form']= form_contact
    return render(request, 'home.html', context)

def contact(request):
    context = {}
    form_contact = ContactForm(request.POST or None)
    if request.method == "POST":
        if form_contact.is_valid():
            form_contact.save()
            return redirect('blog:contact')

    context['form'] = form_contact
    return render(request, 'blog/contact.html', context)
