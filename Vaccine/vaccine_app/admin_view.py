from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render

from vaccine_app.filter import Admin_Hospital_filter
from vaccine_app.form import Hospital_reg, Vaccine_reg, User_reg, Nurse_reg
from vaccine_app.models import Hospital, Vaccine, User, Nurse, Complaints, Vaccineshedule, Vaccine_Appointment


#hospital CRUD
#ADD
@login_required(login_url='sigin_in1')
def hospital_add(request):
    hosp_form = Hospital_reg()
    if request.method == 'POST':
        hosp_form = Hospital_reg(request.POST)
        if hosp_form.is_valid():
            hosp_form.save()
            return redirect('display')
    return render(request,'admin/hospital_add.html',{'hosp_form':hosp_form})

#DELETE
@login_required(login_url='sigin_in1')
def hospital_delete(request,id):
    hosp_del = Hospital.objects.get(id=id)
    hosp_del.delete()
    return redirect('display')

#EDIT
@login_required(login_url='sigin_in1')
def hospital_edit(request,id):
    hosp_data = Hospital.objects.get(id=id)
    if request.method == 'POST':
        upd_form=Hospital_reg(request.POST,instance=hosp_data)
        if upd_form.is_valid():
            upd_form.save()
            return redirect('display')
    else:
        upd_form = Hospital_reg(instance=hosp_data)
    return render(request,'admin/update_hosp_form.html',{'upd_form':upd_form})

#DISPLAY
@login_required(login_url='sigin_in1')
def hospital_display(request):
    hospital_data = Hospital.objects.all()
    hospitalFilter = Admin_Hospital_filter(request.GET,queryset=hospital_data)
    hospital_data = hospitalFilter.qs
    return render(request,'admin/hospital_display.html',{'hospital_data':hospital_data,'hospitalFilter':hospitalFilter})

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#VACCINE
#CRUD
#ADD
@login_required(login_url='sigin_in1')
def vaccine_add(request):
    vacc_form = Vaccine_reg()
    if request.method == 'POST':
        vacc_form=Vaccine_reg(request.POST)
        if vacc_form.is_valid():
            vacc_form.save()
            return redirect('vaccineDisplay')
    return render(request,'admin/vaccine_add.html',{'vacc_form':vacc_form})

#DELETE
@login_required(login_url='sigin_in1')
def vaccine_delete(request,id):
    del_vacc = Vaccine.objects.get(id=id)
    del_vacc.delete()
    return redirect('vaccineDisplay')

#EDIT
@login_required(login_url='sigin_in1')
def vaccine_edit(request,id):
    vacc_data = Vaccine.objects.get(id=id)
    if request.method =='POST':
        upd_vform=Vaccine_reg(request.POST,instance=vacc_data)
        if upd_vform.is_valid():
            upd_vform.save()
            return redirect('vaccineDisplay')
    else:
        upd_vform= Vaccine_reg(instance=vacc_data)
    return render(request,'admin/vaccine_update_form.html',{'upd_vform':upd_vform})

#DISPLAY
@login_required(login_url='sigin_in1')
def vaccine_display(request):
    vaccine_data = Vaccine.objects.all()
    return render(request,'admin/vaccine_display.html',{'vaccine_data':vaccine_data})

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Nurse Display
@login_required(login_url='sigin_in1')
def nurse_display(request):
    nurse_data = Nurse.objects.all()
    return render(request,'admin/nurse_display.html',{'nurse_data':nurse_data})

#Nurse Delete
@login_required(login_url='sigin_in1')
def nurse_del(request,id):
    nurse_dele = Nurse.objects.get(id=id)
    nurse_dele.delete()

#Nurse edit
@login_required(login_url='sigin_in1')
def nurse_edit(request,id):
    nurse_upd = Nurse.objects.get(id=id)
    if request.method == 'POST':
        upd_form = Nurse_reg(request.POST, instance=nurse_edit)
        if upd_form.is_valid():
            upd_form.save()
            return redirect('nurse_display')
    else:
        upd_form = Nurse_reg(instance=nurse_edit)
    return render(request,)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------


#User Display
@login_required(login_url='sigin_in1')
def user_display(request):
    user_data = User.objects.all()
    return render(request, 'admin/user_display.html', {'user_data': user_data})

#User delete
@login_required(login_url='sigin_in1')
def user_del(request,id):
    user_dele =User.objects.get(id=id)
    user_dele.delete()
    return redirect('user_display')

#User edit
@login_required(login_url='sigin_in1')
def user_edit(request,id):
    user_up = User.objects.get(id=id)
    if request.method == 'POST':
        upd_form = User_reg(request.method, instance=user_up)
        if upd_form.is_valid():
            upd_form.save()
        else:
            upd_form = User_reg(instance=user_up)
        return render(request,'admin/')



#Complaint display
@login_required(login_url='sigin_in1')
def user_Complaint(request):
    compalint_data = Complaints.objects.all()
    return render(request,'admin/complaint_display.html',{'compalint_data':compalint_data})

#Complaint Reply
@login_required(login_url='sigin_in1')
def complaint_reply(request,id):
    comp_reply = Complaints.objects.get(id=id)
    if request.method == 'POST':
        re = request.POST.get('reply')
        comp_reply.reply = re
        comp_reply.save()
        return redirect('complaint1')
    return render(request,'admin/compliant_reply_form.html',{'comp_reply':comp_reply})

#Shedule List
@login_required(login_url='sigin_in1')
def admin_schedule_list(request):
    sa = Vaccineshedule.objects.all()
    return render(request,'admin/schedule_display_admin.html',{'sa':sa})

#Appointment reply
@login_required(login_url='sigin_in1')
def appointment_req_list_display(request):
    adata = Vaccine_Appointment.objects.all()
    return render(request,'admin/appointment_reply.html',{'adata':adata})

@login_required(login_url='sigin_in1')
def appointment_accept(request,id):
    acc_data = Vaccine_Appointment.objects.get(id=id)
    obj = acc_data
    obj.status = 1
    obj.save()
    return redirect('appointment_req_list_display1')

@login_required(login_url='sigin_in1')
def appointment_decline(request,id):
    acc_data = Vaccine_Appointment.objects.get(id=id)
    obj = acc_data
    obj.status = 2
    obj.save()
    return redirect('appointment_req_list_display1')


















