from django_filters import FilterSet
from .models import Response


class CustomFilter(FilterSet):

    class Meta:
        model = Response
        fields = {
            'product': ['exact']
        }