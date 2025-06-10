import django_filters
from django import forms
from django_filters import CharFilter
from app.models import Tasks


class TaskFilter(django_filters.FilterSet):
    title =CharFilter(field_name='title',label='',lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder':'Search by Title' , 'class' : 'form-control'
    }))

    class Meta:
        model = Tasks
        fields =('title',)
