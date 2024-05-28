import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['exact', 'gte', 'lte', 'lt'],  # exact match, greater than or equal to, less than or equal to
            'name': ['icontains'],  # case-insensitive containment
        }
