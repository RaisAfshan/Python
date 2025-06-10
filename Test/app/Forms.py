from django.contrib.auth.forms import UserCreationForm
from django import forms
from app.models import CustomUser, TaskUser, Tasks


class CustomUser_Reg(UserCreationForm):
    username =forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username','password1','password2']

class UserRegister(forms.ModelForm):
    class Meta:
        model = TaskUser
        fields =['name','email','phone_number']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title','description','completed']