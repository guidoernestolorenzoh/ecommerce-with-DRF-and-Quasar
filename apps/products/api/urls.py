from itertools import product

from django.urls import path
from apps.products.api.views.general_views import IndicatorList, IndicatorDetail, CategoryProductList, \
    CategoryProductDetail, MeasureUnitList, MeasureUnitDetail
from apps.products.api.views.product_views import ProductList, ProductDetail
from apps.products.models import Product

urlpatterns = [

    # path('indicator/', IndicatorList.as_view(), name='indicator_list'),
    # path('indicator/<int:pk>/', IndicatorDetail.as_view(), name='indicator_detail'),
    #
    # path('category_product/', CategoryProductList.as_view(), name='category_product_list'),
    # path('category_product/<int:pk>/', CategoryProductDetail.as_view(), name='category_product_detail'),
    #
    # path('measure_unit/', MeasureUnitList.as_view(), name='measure_unit_list'),
    # path('measure_unit/<int:pk>/', MeasureUnitDetail.as_view(), name='measure_unit_detail'),

    # path('product/', ProductList.as_view(), name='product_list'),
    # path('product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),

]