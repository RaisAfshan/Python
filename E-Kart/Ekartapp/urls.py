from django.urls import path
from Ekartapp import views, admin_views

urlpatterns=[

#Views
    path('',views.index,name='index'),
    path('Register',views.userRegisteration, name='Register1'),
    path('login',views.loginUser,name='login1'),
    path('logout',views.logout_view,name='logout1'),

#Admin Views
    path('admin_dashboard',admin_views.admin_dashboard, name='adminDash'),

    #Category CRUD
    path('category_display',admin_views.categoryDisplay,name='categoryDisplay'),
    path('category_form',admin_views.category_view,name='categoryForm'),
    path('category_edit/<int:id>',admin_views.category_edit,name='categoryEdit'),
    path('category_delete/<int:id>',admin_views.category_delete,name='categoryDelete'),

    #

]