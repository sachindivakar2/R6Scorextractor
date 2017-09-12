from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^simple_upload/', views.simple_upload, name='simple_upload'),
	
	
]
