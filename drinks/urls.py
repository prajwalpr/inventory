from django.conf.urls import url

from .import views

app_name = "drinks"

urlpatterns = [
    url(r'^$', views.drinks_list, name="list"),
    url(r'^create/$', views.drinks_create, name="drinks_create"),
]
