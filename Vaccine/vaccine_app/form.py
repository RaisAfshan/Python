from django import forms
from django.contrib.auth.forms import UserCreationForm


from vaccine_app.models import Hospital, Vaccine, CustomUser, Nurse, User, Complaints, Vaccineshedule


class DateInput(forms.DateInput):
    input_type = 'date'

class Timeinput(forms.TimeInput):
    input_type = 'time'

class Hospital_reg(forms.ModelForm):
    class Meta:
        model =Hospital
        fields = ('name','contact_no','place','email')

class Vaccine_reg(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields =('vaccine_name','vaccine_type','description')

class CustomUser_reg(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class Nurse_reg(forms.ModelForm):
    class Meta:
        model=Nurse
        fields=('name','contact_no','email','address','hospital')

class User_reg(forms.ModelForm):
    class Meta:
        model=User
        fields = ('name','contact_no','address','child_name','child_age','recent_vaccination')

class Complaint_reg(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Complaints
        fields =('subject','complaint','date')

class VaccineShedule_reg(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=Timeinput)
    end_time = forms.TimeField(widget=Timeinput)
    class Meta:
        model = Vaccineshedule
        fields = ('vaccine','date','start_time','end_time')




