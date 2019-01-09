from django.conf.urls import url

from .import views

app_name = "drinks"

urlpatterns = [
    url(r'^$', views.drinks_list, name="drinks_list"),
    url(r'^create/$', views.drinks_create, name="drinks_create"),
    url(r'^(?P<id>\d+)/view/$', views.drinks_view, name="drinks_view"),
    url(r'^(?P<id>\d+)/edit/$', views.drinks_edit, name="drinks_edit"),
    url(r'^(?P<id>\d+)/delete/$', views.drinks_delete, name="drinks_delete"),

]
