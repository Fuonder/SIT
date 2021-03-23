from django.urls import path

from . import views

urlpatterns = [
	path('page1', views.index, name ='site1.html'),
	path('page2', views.index2, name='site2.html'),
]
