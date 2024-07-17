from django_filters import FilterSet, DateFilter
from .models import Post
from django.forms import DateInput
from django import forms


class PostFilter(FilterSet):
    post_time = DateFilter(
        field_name='post_time',
        widget=DateInput(attrs={'type': 'date'}),
        label='Дата',
        lookup_expr='date__gte',
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact']
        }
