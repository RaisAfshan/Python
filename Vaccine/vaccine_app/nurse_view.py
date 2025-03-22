from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from vaccine_app.form import Complaint_reg, VaccineShedule_reg
from vaccine_app.models import Nurse, Vaccineshedule, Vaccine_Appointment


#Complaint Nurse form
@login_required(login_url='sigin_in1')
def Complaint_nurse(request):
    form = Complaint_reg()
    u = request.user
    if request.method == 'POST':
        form = Complaint_reg(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            return redirect('vaccine_schedule_display_list1')
    return render(request,'nurse/nComplaint_add_form.html',{'form':form})

#Dashboard Nurse
@login_required(login_url='sigin_in1')
def dashboard_nurse(request):
    u = request.user
    nurse_data = Nurse.objects.get(user=u)
    return render(request,'Nurse/nurse_dashboard.html',{'nurse_data':nurse_data})

#Sheduling Vaccine
@login_required(login_url='sigin_in1')
def scheduling_vaccine(request):
    form = VaccineShedule_reg
    n = request.user
    d = Nurse.objects.filter(user=n).first()
    u = d.hospital
    if request.method == 'POST':
        form =VaccineShedule_reg(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.hospital_name = u
            obj.save()
            return redirect('vaccine_schedule_display_list1')
    return render(request,'Nurse/schedule_add.html',{'form':form})

#scheduled_vaccine_display
@login_required(login_url='sigin_in1')
def vaccine_schedule_display(request):
    vaccine_schedule_data = Vaccineshedule.objects.all()
    return render(request,'Nurse/nurse_schedule_display.html',{'vaccine_schedule_data':vaccine_schedule_data})

#Schedule vaccine delete
@login_required(login_url='sigin_in1')
def vaccine_schedule_delete(request,id):
    vaccine_schedule_delete = Vaccineshedule.objects.get(id=id)
    vaccine_schedule_delete.delete()
    return redirect('vaccine_schedule_display_list1')

#Schedule vaccine edit
@login_required(login_url='sigin_in1')
def vaccine_schedule_edit(request,id):
    vaccine_schedule_data = Vaccineshedule.objects.get(id=id)
    if request.method == 'POST':
        upd_form = VaccineShedule_reg(request.POST,instance=vaccine_schedule_data)
        if upd_form.is_valid():
            upd_form.save()
            return redirect('vaccine_schedule_display_list1')
    else:
        upd_form = VaccineShedule_reg(instance=vaccine_schedule_data)
    return render(request,'Nurse/vaccine_schedule_edit.html',{'upd_form':upd_form})

#Profile nurse
@login_required(login_url='sigin_in1')
def nurse_profile(request):
    u = request.user
    profile_data = Nurse.objects.get(user=u)
    return render(request,'Nurse/nurse_profile.html',{'profile_data':profile_data})

#Approved Appointment
@login_required(login_url='sigin_in1')
def approved_appointment(request):
    accepted_data = Vaccine_Appointment.objects.filter(status=1).order_by('schedule__hospital_name__name') # -schedule__hospital_name__name give '-' inside order_by will reverse the order
    return render(request,'Nurse/approved_appointment_display.html',{'accepted_data':accepted_data})







