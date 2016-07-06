from django.conf.urls import url
from django.contrib import admin

from patient import views as patientviews
from django.contrib.auth import views
from patient.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', patientviews.homepage, name = 'homepage'),
    # url(r'^login/$', views.login, {'login_template':'login.html', 'authentication_form':LoginForm}),
    url(r'^login/$',views.login,{'template_name':'login.html','authentication_form':LoginForm}),

    url(r'^logout/$', views.logout,{'next_page': '/'}),
    url(r'^mainpage/$', patientviews.mainpage, name='mainpage'),
    url(r'^patient/$', patientviews.formpage, name = 'formpage'),
    url(r'^severitydoc/$', patientviews.doc, name = 'docpage'),
]
