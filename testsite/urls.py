from django.conf.urls import url
from django.contrib import admin

from patient import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'mainpage'),
    url(r'^patient/$', views.formpage),
    url(r'^severitydoc/$', views.doc)
]
