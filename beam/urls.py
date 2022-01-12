from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('reset', views.reset, name='reset'),
    path('report', views.report, name='report'),
]