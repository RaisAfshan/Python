
from django import forms
from django.contrib.auth.forms import UserCreationForm

from Ekartapp.Choices import GENDER_CHOICES
from Ekartapp.models import Custom_User, UserModel, Category, Product, UserAddress, VariantType, Variants, \
    ProductVariant, ProductVariantImage, Coupons, OrderItem, Order, CarouselImage


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

        labels = {
            'name':'Category Name',
            'parent':'Parent Category',
        }

        help_texts = {
            'name':'Enter the name of the category (e.g., Electronics, Clothing)',
            'parent':'Select a parent category if this a sub-category. Leave blank for a top-level category'
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder':'e.g. Electronics, Clothing',
                'class':'form-control'
            }),
            'parent':forms.Select(attrs={
                'class':'form-select'
            })
        }

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)

        self.fields['parent'].queryset = Category.objects.filter(parent__isnull=True, status=True)

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('brand','title','description','status','category','primary_variant','secondary_variant')
        labels = {
            'brand':'Brand Name',
            'title':'Product Title',
            'description':'Product Description',
            'status':'Active Status',
            'category':'Product Category',
            'primary_variant':'Primary Variant',
            'secondary_variant':'Secondary Variant'
        }

        help_texts = {
            'brand':'Enter the brand of the product (e.g.,Samsung,Nike).',
            'title':'Enter the product title (e.g., Galaxy S21,Running Shoe).',
            'description':'Write a  short description of the product.',
            'status':'Tick this box if the product is active and visible on the store.',
            'category':'Select the sub-category this product belong to.',
            'primary_variant':'Select the main variant type (e.g., Color, Size).',
            'secondary_variant':'Optional: Select a secondary variant type if applicable.'
        }

        widgets = {
            'brand': forms.TextInput(attrs={'placeholder':'Enter brand name', 'class':'form-control'}),
            'title':forms.TextInput(attrs={'placeholder':'Enter product title','class':'form-control'}),
            'description':forms.Textarea(attrs={'placeholder':'Enter product description','class':'form-control','row':3}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'primary_variant': forms.Select(attrs={'class': 'form-select'}),
            'secondary_variant': forms.Select(attrs={'class': 'form-select'}),
        }


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['category'].queryset = Category.objects.filter(parent__isnull=False,status=True)

class VariantTypeForm(forms.ModelForm):
    class Meta:
        model = VariantType
        fields = ('name','status')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder':'e.g. Color or Size',
                'class':'form-control'
            }),
            'status':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }
        labels = {
            'name':'Variants Type Name',
            'status':'Active Status',
        }


class VariantsForm(forms.ModelForm):
    class Meta:
        model = Variants
        fields = ['value','variant_type','status']

        labels = {
            'value':'Variant Value',
            'variant_type':'Variant Type',
            'status':'Active Status',
        }

        help_texts = {
            'value':'Enter the actual value for this variant, such as "Red","Large" or "128GB".',
            'variant_type':'Select which Variant Type this value belongs to (e.g., Color, Size).',
            'status':'Tick this box if the variant value should be visible '
        }

        widgets = {
            'value':forms.TextInput(attrs={
                'placeholder':'e.g. Red, Large, 128GB',
                'class':'form-control'
            }),
            'variant_type':forms.Select(attrs={
                'class':'form-select'
            }),
            'status':forms.CheckboxInput(attrs={
                'class':'form-check-input'
            }),
        }


class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ('primary_variant', 'secondary_variant', 'price', 'quantity', 'is_default', 'variant_status')
        widgets = {
            'primary_variant': forms.Select(attrs={'class': 'form-select'}),
            'secondary_variant': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter price', 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Enter quantity', 'class': 'form-control'}),
            'is_default': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'variant_status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        help_texts = {
            'is_default': 'Set as default variant.',
            'variant_status': 'Active status.',
        }



class ProductVariantImageForm(forms.ModelForm):
    class Meta:
        model = ProductVariantImage
        fields = ('image','is_default')

        widgets ={
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'is_default':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

        help_texts = {
            'image':'Upload product image (JPG, JPEG, PNG, GIF).',
            'is_default':'Set as default image.'
        }

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

class CarouselImageForm(forms.ModelForm):
    class Meta:
        model = CarouselImage
        fields = '__all__'

        help_texts = {
            'title': 'Enter a short title for the image',
            'image': 'Upload an image file (JPG,JPEG,PNG,GIF).',
            'is_active': 'Check to make this image visible in the carousel.',
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter image title', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class userAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ('address_type','home_name','street_address','city','state','country','zip_code','is_default')

        labels ={
            'address_type':'Address Type',
            'home_name':'Home/Building Name',
            'street_address':'Street Address',
            'city':'City',
            'state':'State',
            'country':'Country',
            'zip_code':'Zip Code',
            'is_default':'Default Address',
        }

        help_texts = {
            'address_type':'Select type: Home, Office, etc',
            'home_name':'Enter house or building name/number.',
            'street_address': 'Enter the street or area name.',
            'city': 'Enter your city.',
            'state': 'Enter your state/province.',
            'country': 'Enter your country.',
            'zip_code': 'Enter postal/zip code.',
            'is_default': 'Check if this is your default address.',
        }

        widgets = {
            'address_type': forms.Select(attrs={'class': 'form-select'}),
            'home_name': forms.TextInput(attrs={'placeholder': 'e.g., Building A, House 23', 'class': 'form-control'}),
            'street_address': forms.TextInput(attrs={'placeholder': 'e.g., 5th Avenue, MG Road', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter city', 'class': 'form-control'}),
            'state': forms.TextInput(attrs={'placeholder': 'Enter state', 'class': 'form-control'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter country', 'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'Enter postal/zip code', 'class': 'form-control'}),
            'is_default': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }



