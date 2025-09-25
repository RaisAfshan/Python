from django.urls import path
from Ekartapp import views
urlpatterns=[
    path('',views.index,name='index'),
]