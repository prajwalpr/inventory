from django.conf.urls import url

from . import views

app_name = "blog"

urlpatterns = [
    url(r'^contact/$', views.contact, name="contact"),
]
