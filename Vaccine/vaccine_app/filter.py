import django_filters
from django import forms
from django.db.models import Q
from django_filters import CharFilter
from vaccine_app.models import Hospital, Vaccineshedule


#Admin
class Admin_Hospital_filter(django_filters.FilterSet):
    name = CharFilter(field_name='name',label='',lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder':'Search hospital', 'class':'form-control'
    }))
    #field_name should be the field in model
    #lookup_expr = 'icontains' to make both hospital name in table and input from the search box in lowercase
    #widget = to style the search form
    class Meta:
        model = Hospital
        fields = ('name',) # if there is only one field, then give comma after the feild

#User
class Vaccineshedule_filter(django_filters.FilterSet):
   searchShedule = CharFilter(method='filter_by_all',label='',widget=forms.TextInput(attrs={
       'placeholder': 'Search ', 'class': 'form-control'
   }))
   class Meta:
       model = Vaccineshedule
       fields = []

   def filter_by_all(self,queryset,name,value):
        return queryset.filter(
            Q(vaccine__vaccine_name__icontains = value) |
            Q(hospital_name__name__icontains = value)

        )



