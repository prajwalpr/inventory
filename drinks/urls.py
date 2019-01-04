from django.conf.urls import url

from .import views

app_name = "drinks"

urlpatterns = [
    url(r'^beer/$', views.beer , name="beer"),
]
