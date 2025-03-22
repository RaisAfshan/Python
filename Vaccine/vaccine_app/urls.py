from tkinter.font import names

from . import views, admin_view, user_view, nurse_view
from django.urls import path

urlpatterns = [

    #VIEW
    path('',views.home,name='home1'),
    path('admindash',views.admin_dasboard,name='admindash'),
    path('userReg',views.user_login,name='userReg'),
    path('nurseReg',views.nurse_login,name='nurseReg'),
    path('sigin_in',views.Sign_in,name='sigin_in1'),
    path('logOut',views.logout_view,name='lodOut1'),
    path('register',views.register,name='register1'),
    path('dash-home',views.dash_home,name='dash_home1'),

    #-------------------------------------------------------------------------------------------------------------------------------------------------

    #-----ADMIN VIEW-----
    #hospital url
    path('add_hospital',admin_view.hospital_add,name='add_hospital'),
    path('display',admin_view.hospital_display,name='display'),
    path('hosp_delete/<int:id>',admin_view.hospital_delete,name='hosp_delete'),
    path('hosp_edit/<int:id>',admin_view.hospital_edit,name='hosp_edit'),

    #Vaccine url
    path('add_vaccine',admin_view.vaccine_add,name='add_vaccine'),
    path('vaccineDelete/<int:id>',admin_view.vaccine_delete,name='vaccineDelete'),
    path('vaccineEdit/<int:id>',admin_view.vaccine_edit, name='vaccineEdit'),
    path('vaccineDisplay',admin_view.vaccine_display,name='vaccineDisplay'),

    #User url
    # path('add_user',admin_view.user_add,name='add_user'),
    path('user_display',admin_view.user_display,name='user_display'),
    # path('user_del/<int:id>',admin_view.user_del,name='user_del'),
    # path('user_edit/<int:id>',admin_view.user_edit,name='user_edit'),

    #Nurse url
    # path('add_nurse',admin_view.nurse_add,name='add_nurse'),
    path('nurse_display',admin_view.nurse_display,name='nurse_display'),
    # path('nurse_edit/<int:id>',admin_view.nurse_edit,name='nurse_edit'),
    # path('nurse_delete/<int:id>',admin_view.nurse_del,name='nurse_delete'),

    #Complaint url
    path('complaint',admin_view.user_Complaint,name='complaint1'),
    path('complaintReply/<int:id>',admin_view.complaint_reply,name='complaintReply1'),

    #Schedule url
    path('admin-schedule-list',admin_view.admin_schedule_list,name='admin-schedule-list1'),

    #Appointment url
    path('appointment-req-list-display',admin_view.appointment_req_list_display,name='appointment_req_list_display1'),
    path('appointment-accept/<int:id>',admin_view.appointment_accept,name='appointment_accept1'),
    path('appointment-decline/<int:id>',admin_view.appointment_decline,name='appointment_decline1'),


    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #----- USER VIEW----
    path('userdash',user_view.user_dash,name='userdash1'),

    #Complaint url
    path('users_complaint',user_view.complaint_user,name='users_complaint1'),
    path('complaint_display_user',user_view.complaint_user_display,name='complaint_display_user1'),

    #Vaccine Schedule url
    path('user-schedule-list',user_view.user_vaccine_sch_disp,name='user-schedule-list1'),

    #User Profile
    path('User-Profile',user_view.user_profile,name='User-Profile1'),

    #Vaccine Appointment
    path('req-appointment/<int:id>',user_view.req_appointment,name='req_appointment1'),
    path('appointment-status',user_view.appointment_status,name='appointment_status1'),

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------

    #----NURSE VIEW----
    path('nurse_dash',nurse_view.dashboard_nurse,name="nurse_dash1"),
    path('complaint_form',nurse_view.Complaint_nurse,name='complaint_form1'),

    #Nurse Profile
    path('nurse-profile',nurse_view.nurse_profile,name='nurse-profile1'),

    #CRUD for vaccine_scheduling
    path('schedule_vaccine',nurse_view.scheduling_vaccine,name='schedule_vaccine1'),
    path('vaccine_schedule_display_list',nurse_view.vaccine_schedule_display,name='vaccine_schedule_display_list1'),
    path('vaccine-schedule-delete/<int:id>',nurse_view.vaccine_schedule_delete,name='vaccine-schedule-delete1'),
    path('vaccine-schedule-edit/<int:id>',nurse_view.vaccine_schedule_edit,name='vaccine-schedule-edit1'),

    #VACCINE approved list
    path('approved-appointment',nurse_view.approved_appointment,name='approved_appointment1')


]