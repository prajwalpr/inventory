from django.conf.urls import url

from . import views

app_name = "category"

urlpatterns = [
    url(r'^$', views.category_list, name="category_list"),
    url(r'^create/$', views.category_create, name="category_create"),
    url(r'^(?P<pk>\d+)/edit/$', views.category_edit, name="category_edit"),
    url(r'^(?P<pk>\d+)/delete/$', views.category_delete, name='category_delete'),
]
