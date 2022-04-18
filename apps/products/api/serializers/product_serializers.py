from email.mime import image

from django.conf import settings
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from apps.products.api.serializers.general_serializers import MeasureUnitSerializer
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image.url if instance.image != '' else 'products/default.png',
            'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
            'category_product': instance.category_product.description if instance.category_product is not None else '',
            # 'owner': instance.owner.username if instance.owner is not None else '',
        }
