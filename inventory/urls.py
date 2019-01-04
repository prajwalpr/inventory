from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from blog.views import home, ajax
from blog.views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    # url(r'^ajax/', ajax, name='ajax'),
    url(r'^users/', include('users.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^category/', include('category.urls')),
    url(r'^drinks/', include('drinks.urls')),
    url(r'^units/', include('units.urls')),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
