from django.urls import path

from app import views

urlpatterns=[
    path('', views.userLogin,name='log'),
    path('user_dash',views.user_dash,name='user_dash1'),
    path('user_regForm',views.user_regForm,name='user_regForm1'),
    path('logout',views.logOut,name='logOut'),

    path('addTask',views.addTask,name='addTask1'),
    path('TaskList',views.TaskList,name='TaskList1'),
    path('Task_edit/<int:id>',views.Taskedit,name='Task_edit1'),
    path('taskDelete/<int:id>',views.taskDelete,name='taskDelete1')
]