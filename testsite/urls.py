from django.conf.urls import url
from django.contrib import admin

from patient import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'Main page'),
    url(r'^patient/$', views.formpage, name = 'Patient Form'),
    url(r'^severitydoc/$', views.doc, name = 'Severity Documentation')
]
