from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from drinks.models import Drinks
from .forms import DrinksForm
from category.models import Category


# Create your views here.

def drinks_list(request):
    # print(request.GET.get('category'))
    category = Category.objects.get(id=request.GET.get('category'))
    # data = Drinks.objects.filter(cid=category)
    drinks_list = category.drinks.all()
    return render(request, "drinks/drinks_list.html", {'drinks_list': drinks_list})


def drinks_create(request):
    form = DrinksForm(request.POST or None, request.FILES or None)


    if request.method == 'POST':
        try:
            category = Category.objects.get(id=request.GET.get('category'))
        except:
            messages.error(request, "some message")
            return redirect("category:category_list")

        if form.is_valid():
            # print(type(form.cleaned_data.get('category')))
            drinks = form.save(commit=False)
            drinks.cid = category
            drinks.save()
            messages.success(request, 'Drinks added')
            return redirect('drinks:drinks_create')

    context = {
        'form': form
    }

    return render(request, 'drinks/drinks_create.html', context)


def drinks_delete(request, id):
    try:
        data = Drinks.objects.get(id=id)
        if request.method == 'POST':
            data.delete()
            return redirect(reverse('drinks:drinks_list') + '?category=' + str(data.cid.id))
        return render(request, 'drinks/drinks_delete.html', {'data': data})

    except Drinks.DoesNotExist:
        messages.error(request, 'Data doesnot found')
        return render(request, 'drinks/drinks_delete.html', {'data': data})


def drinks_edit(request, id):
    try:
        data = Drinks.objects.get(id=id)
    except Drinks.DoesNotExist:
        messages.error(request, 'Data doesnot found')
        return redirect('drinks:drinks_list')
    # form = DrinksForm(data=request.POST or None , instance=data, files=request.FILES or None)
    form = DrinksForm(instance=data)
    if request.method == 'POST':
        # form = DrinksForm(request.POST, request.FILES)
        form = DrinksForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            dri = form.save(commit=False)
            dri.save()
            return redirect(reverse('drinks:drinks_list') + '?category='+ str(data.cid.id))
    return render(request, 'drinks/drinks_edit.html', {'form': form})


def drinks_view(request, id):
    drinks_view = Drinks.objects.get(id=id)
    return render(request, 'drinks/drinks_view.html', {'drinks_view': drinks_view})

