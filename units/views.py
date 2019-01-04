from django.shortcuts import render, redirect, get_object_or_404
from .forms import UnitForm
from django.contrib import messages
from django.http import Http404
from .models import Units


# Create your views here.
def unit_list(request):
    unit_list = Units.objects.all().order_by("name")
    return render(request, 'units/unit_list.html', {'unit_list': unit_list})

def unit_create(request):
    form = UnitForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            unit = form.save(commit=False)
            unit.save()
            messages.success(request, 'Successfully unit is saved...')
            return redirect('units:unit_create')
    return render(request, 'units/unit_create.html', {'form': form})

def unit_delete(request, pk):
    try:
        unit = Units.objects.get(pk=pk)
    except Units.DoesNotExist:
        raise Http404

    if request.method == "POST":
        unit.delete()
        return redirect('units:unit_list')

    context = {
        'unit' : unit
    }

    return render(request, 'units/unit_delete.html', context)

def unit_edit(request, pk):
    unit = get_object_or_404(Units, id=pk)
    if request.method == 'POST':
        form = UnitForm(request.POST, instance= unit)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.save()
            return redirect('units:unit_list')

    else:
        form = UnitForm(instance=unit)
    return render(request, 'units/unit_edit.html', {'form': form})
