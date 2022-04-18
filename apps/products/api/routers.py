from rest_framework.routers import DefaultRouter
from apps.products.api.views.general_views import IndicatorViewSet, CategoryProductViewSet, MeasureUnitViewSet
from apps.products.api.views.product_views import ProductViewSet
from apps.users.api.api import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'indicators', IndicatorViewSet, basename='indicators')
router.register(r'category_products', CategoryProductViewSet, basename='category_products')
router.register(r'measure_units', MeasureUnitViewSet, basename='measure_units')




urlpatterns = router.urls

