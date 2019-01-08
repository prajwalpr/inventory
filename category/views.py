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
    form = CategoryForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created.')
            return redirect("category:category_create")

    context = {
        'form': form
    }
    return render(request, 'category/create.html', context)


def category_edit(request, pk):
    try:
        data = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        messages.error(request, 'Data doesnot found')
        return redirect('category:category_list')
    form = CategoryForm(instance=data)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.save()
            return redirect('category:category_list')
    return render(request, 'category/category_edit.html', {'form': form})


def category_delete(request, pk):
    try:
        data = Category.objects.get(pk=pk)
        if request.method == "POST":
            data.delete()
            return redirect('category:category_list')
        return render(request, 'category/category_delete.html', {'data': data})

    except Category.DoesNotExist:
        messages.error(request, 'Data doesnot found')
        return render(request, 'category/category_delete.html', {'data': data})


