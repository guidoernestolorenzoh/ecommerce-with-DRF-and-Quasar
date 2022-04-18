from rest_framework import serializers
from apps.products.models import MeasureUnit, CategoryProduct, Indicator




class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')



class IndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicator
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')



    def to_representation(self, instance):
        return{
            'id': instance.id,
            'discount_value': instance.discount_value,
            'category_product': instance.category_product.description,
        }

    # def validate(self, data):
    #     if data["start_date"] > data["order_date"]:
    #         raise serializers.ValidationError({'error': "rango de fecha invalido"})
    #
    #     return data


class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')