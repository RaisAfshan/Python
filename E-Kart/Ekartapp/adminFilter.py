import django_filters
from django import forms
from django.db.models import Q
from django_filters import CharFilter

from Ekartapp.models import ProductVariant


class ProductVariantFilter(django_filters.FilterSet):
    variantSearch = CharFilter(method='filter_by_all',label='',widget=forms.TextInput(attrs={'placeholder':'Search product name','class':'form-control'}))
    class Meta:
        model = ProductVariant
        fields = []

    def filter_by_all(self,queryset,name,value):
        return queryset.filter(
            Q(product__title__icontains=value) |
            Q(product__brand__icontains=value)
        ).distinct()
