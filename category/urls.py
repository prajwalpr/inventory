from django.conf.urls import url

from . import views

app_name = "category"

urlpatterns = [
    url(r'^$', views.category_list, name="list"),
    url(r'^create/$', views.category_create, name="create"),
    url(r'^(?P<pk>\d+)/edit/$', views.category_edit, name="edit"),
    url(r'^(?P<pk>\d+)/delete/$', views.category_delete, name='delete'),
    url(r'^(?P<pk>\d+)/drinks/$', views.drinks, name='drinks'),
    url(r'^(?P<pk>\d+)/new/$', views.new, name='new'),
]
