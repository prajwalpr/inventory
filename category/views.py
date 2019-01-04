import json

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category
from drinks.forms import DrinksForm
from django.http import HttpResponse

from .forms import CategoryForm
# Create your views here.

def category_list(request):
    data = Category.objects.all()
    return render(request, 'category/category_list.html', {'data': data})

def category_create(request):
    form = CategoryForm(request.POST or None , request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created.')
            return redirect("category:create")

    context = {
        'form' : form
    }
    return render(request, 'category/create.html', context)


def category_edit(request, pk):
    try:
        data = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        messages.error(request, 'Data doesnot found')
        return redirect('category:list')
    form = CategoryForm(instance=data)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.save()
            return redirect('category:list')
    return render(request, 'category/category_edit.html', {'form': form})


def category_delete(request, pk):
    try:
        data = Category.objects.get(pk = pk)
        if request.method == "POST":
            data.delete()
            return redirect('category:list')
        return render(request, 'category/category_delete.html', {'data': data})

    except Category.DoesNotExist:
        messages.error(request, 'Data doesnot found')
        return render(request, 'category/category_delete.html', {'data': data})


def drinks(request, pk):
    data = Category.objects.get(pk = pk)
    return render(request, 'category/drinks.html', {'data': data})

def new(request, pk):
    data = Category.objects.get(pk = pk)
    return render(request, 'category/new.html', {'data': data})
