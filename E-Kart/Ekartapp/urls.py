from django.urls import path
from Ekartapp import views
urlpatterns=[

    #Views
    path('',views.index,name='index'),
    path('Register',views.userRegisteration, name='Register1'),
    path('login',views.loginUser,name='login1'),
    path('logout',views.logout_view,name='logout1')


]