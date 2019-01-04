from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import DrinksForm
from category.models import Category


# Create your views here.

def drinks_list(request):
    return render(request, "drinks/drinks_beer.html")

def drinks_create(request):
    form = DrinksForm(request.POST or None)
    if request.method == 'POST':
        try:
            category = Category.objects.get(id=request.GET.get('category'))
        except:
            messages.error(request, "some message")
            return redirect("category:list")

        if form.is_valid():
            drinks = form.save(commit=False)
            drinks.cid = category
            drinks.save()
            messages.success(request, 'Drinks added')
            return redirect('drinks:drinks_create')

    context = {
        'form' : form
    }

    return render(request, 'drinks/create_drinks.html', context)


