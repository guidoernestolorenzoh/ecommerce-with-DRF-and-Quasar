# from django.contrib.auth.models import User
import null

from apps.users.models import User
from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords




class MeasureUnit(BaseModel):
    """ Model for Measure Unit"""
    description = models.CharField(
        'Descripcion',
        max_length=50,
        blank=True,
        null=True,
        unique=True
    )
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medidas'

    def __str__(self):
        return self.description



# class Label(models.Model):
#     name = models.CharField(max_length=250)
#
#     def __str__(self):
#         return self.name



class CategoryProduct(BaseModel):
    """ Model for Category"""
    description = models.CharField(
        'Descripcion',
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Categoria de Producto'
        verbose_name_plural = 'Categorias de Productos'

    def __str__(self):
        return self.description



class Indicator(BaseModel):
    """ Model for Indicator"""
    discount_value = models.PositiveSmallIntegerField(
        'Valor de Descuento',
        default=0
    )
    category_product = models.ForeignKey(
        CategoryProduct,
        on_delete=models.CASCADE,
        verbose_name='Categoria'
        )
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicador de Ofertas'

    def __str__(self):
        return f'Oferta de la Categoria {self.category_product}: {self.discount_value}%'


class Product(BaseModel):
    """ Model for Product"""
    name = models.CharField(
        'Nombre de Producto',
        max_length=250,
        null=False,
        blank=False,
        unique=True
    )
    description = models.TextField(
        'Descripcion de Producto',
        null=False,
        blank=False
    )
    image = models.ImageField(
        'Imagen del Producto',
        upload_to='products/',
        default='products/default.png',
        blank=True,
        null=True
    )
    measure_unit = models.ForeignKey(
        MeasureUnit,
        on_delete=models.CASCADE,
        verbose_name='Unidad de Medida'
    )
    category_product = models.ForeignKey(
        CategoryProduct,
        on_delete=models.CASCADE,
        verbose_name='Categoria de Producto'
    )
    owner = models.ForeignKey('users.User', related_name='products', blank=True, null=True, on_delete=models.CASCADE)

    historical = HistoricalRecords()

    # @property
    # def get_image_url(self):
    #     if self.image and hasattr(self.image, 'url'):
    #         return self.image.url
    #     else:
    #         return "/products/products/product.png"

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name


# class Order(models.Model):
#     user = models.ForeignKey(User, models.CASCADE)
#     item = models.ForeignKey(Item, models.CASCADE)
#     start_date = models.DateTimeField(null=True, blank=True)
#     order_date = models.DateTimeField(null=True, blank=True)
#     ordered = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.user.username
