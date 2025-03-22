from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from vaccine_app.filter import Vaccineshedule_filter
from vaccine_app.form import Complaint_reg
from vaccine_app.models import Complaints, User, Vaccineshedule, Vaccine_Appointment


#User Dashboard
@login_required(login_url='sigin_in1')
def user_dash(request):
    u = request.user
    user_data=User.objects.get(user=u)
    print(user_data)
    return render(request,'user/user_dash.html',{'user_data':user_data})

#Complaint Form
@login_required(login_url='sigin_in1')
def complaint_user(request):
    form = Complaint_reg()
    u = request.user
    if request.method == 'POST':
        form = Complaint_reg(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request,'Complaint registered successfully')
            return redirect('userdash1')
    return render(request,'user/complaint_form.html',{'form':form})

#Reply display
@login_required(login_url='sigin_in1')
def complaint_user_display(request):
    n = Complaints.objects.filter(user=request.user)
    return render(request,'user/comp_display_user.html',{'n':n})

#vaccine_schedule_display
@login_required(login_url='sigin_in1')
def user_vaccine_sch_disp(request):
    s = Vaccineshedule.objects.all()
    Vaccine_schedule_filter = Vaccineshedule_filter(request.GET,queryset=s)
    s = Vaccine_schedule_filter.qs
    return render(request,'user/vaccine_schedule_display_user.html',{'s':s,'Vaccine_schedule_filter':Vaccine_schedule_filter})

#User Profile
@login_required(login_url='sigin_in1')
def user_profile(request):
    u = request.user
    profile_data = User.objects.get(user=u)
    return render(request,'user/user_profile.html',{'profile_data':profile_data})

#Vaccine Appointment
@login_required(login_url='sigin_in1')
def req_appointment(request,id):
    schedule = Vaccineshedule.objects.get(id=id)
    u = User.objects.get(user=request.user)
    appointment = Vaccine_Appointment.objects.filter(user=u,schedule=schedule) # if already a schedule is appointed then need to give message that already appointed
    if appointment.exists():
        messages.info(request,'you have already have an appointment at this schedule')
        return redirect('user-schedule-list1')
    else:
        if request.method == 'POST':
            obj = Vaccine_Appointment()
            obj.user = u # to save the data of the appointed user, so that admin can know which user
            obj.schedule = schedule # to save the which schedule that user appointed in Vaccineshedule db
            obj.vaccine_name=schedule.vaccine
            obj.save()
            messages.info(request,'Successfully Appointed')
            return redirect('user-schedule-list1')
        return  render(request,'user/Appointment_ req_form.html',{'schedule':schedule})

#Appointment Status
@login_required(login_url='sigin_in1')
def appointment_status(request):
    u = User.objects.get(user=request.user) # compare current login user to User table to get the user we cannot get directly because User is in Foriegn key
    print(u)
    adata = Vaccine_Appointment.objects.filter(user=u)
    print(adata)
    return render(request,'user/appointment_status_display.html',{'adata':adata})







