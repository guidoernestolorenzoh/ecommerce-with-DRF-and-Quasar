from rest_framework import generics
from apps.products.api.serializers.general_serializers import (
    IndicatorSerializer,
    MeasureUnitSerializer,
    CategoryProductSerializer
)
from apps.base.api import (
    GeneralViewSet
)


# class IndicatorList(GeneralList):
class IndicatorViewSet(GeneralViewSet):
    # queryset = Indicator.objects.filter(state=True)
    serializer_class = IndicatorSerializer


# class IndicatorDetailViewSet(GeneralViewSet):
    # queryset = Indicator.objects.all()
    # serializer_class = IndicatorSerializer


class MeasureUnitViewSet(GeneralViewSet):
    # queryset = MeasureUnit.objects.filter(state=True)
    serializer_class = MeasureUnitSerializer


# class MeasureUnitDetail(GeneralDetail):
    # queryset = MeasureUnit.objects.all()
    # serializer_class = MeasureUnitSerializer


class CategoryProductViewSet(GeneralViewSet):
    # queryset = CategoryProduct.objects.filter(state=True)
    serializer_class = CategoryProductSerializer


# class CategoryProductDetail(GeneralDetail):
    # queryset = CategoryProduct.objects.all()
    # serializer_class = CategoryProductSerializer
