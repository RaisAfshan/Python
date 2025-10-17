
from django import forms
from django.contrib.auth.forms import UserCreationForm

from Ekartapp.Choices import GENDER_CHOICES
from Ekartapp.models import Custom_User, UserModel, Category, Product, UserAddress, VariantType, Variants, \
    ProductVariant, ProductVariantImage, Coupons, OrderItem, Order


class CustomUserForm(UserCreationForm):
    username =forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)


    class Meta:
        model = Custom_User
        fields = ('username','email','password1')

class UserForm(forms.ModelForm):
    gender = forms.ChoiceField(label='Gender', choices= GENDER_CHOICES, required=True, widget=forms.RadioSelect(attrs={'class':'form-check-input mb-3'} ),initial='Male')

    class Meta:
        model = UserModel
        fields = ('fullName','phoneNumber','gender','profilePicture')

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
        fields = ('title','brand','description','status','category','primary_variant','secondary_variant')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['category'].queryset = Category.objects.filter(parent__isnull=False,status=True)

class VariantTypeForm(forms.ModelForm):
    class Meta:
        model = VariantType
        fields = ('name','status')


class VariantsForm(forms.ModelForm):
    class Meta:
        model = Variants
        fields = ['value','variant_type','status']

class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields =('primary_variant','secondary_variant','price','quantity','is_default','status')


class ProductVariantImageForm(forms.ModelForm):
    class Meta:
        model = ProductVariantImage
        fields = ('image','is_default')

class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupons
        fields = '__all__'
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter coupon code'}),
            'discount_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter discount amount'}),
            'discount_percent': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter discount percent'}),
            'expiry_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status','is_seen']

# class OrderItemForm(forms.ModelForm):
#     class Meta:
#         model = OrderItem
#         fields = ['']



class userAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ('address_type','home_name','street_address','city','state','country','zip_code','is_default')




