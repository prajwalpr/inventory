from django.shortcuts import render

# Create your views here.

def beer(request):
    return render(request, "drinks/drinks_beer.html")
