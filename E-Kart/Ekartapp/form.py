
from django import forms
from django.contrib.auth.forms import UserCreationForm

from Ekartapp.Choices import GENDER_CHOICES
from Ekartapp.models import Custom_User, UserModel, Category, Product


class CustomUserForm(UserCreationForm):
    username =forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Custom_User
        fields = ('username','password1','password2')

class UserForm(forms.ModelForm):
    gender = forms.ChoiceField(label='Gender', choices= GENDER_CHOICES, required=True, widget=forms.RadioSelect(attrs={'class':'form-check-input mb-3'} ),initial='Male')

    class Meta:
        model = UserModel
        fields = ('fullName','phoneNumber','gender','profilePicture','email')

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name','parent')

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)

        self.fields['parent'].queryset = Category.objects.filter(parent__isnull=True, status=True)

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title','description','price','status','category')



