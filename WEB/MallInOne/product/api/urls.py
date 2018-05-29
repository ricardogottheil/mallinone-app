
from django.conf.urls import url, include

from .views import ProductRudView, ProductAPIView

urlpatterns = [
    url(r'^$', ProductAPIView.as_view(), name='product-create'),
    url(r'^(?P<pk>\d+)/$', ProductRudView.as_view(), name='product-rud')
]