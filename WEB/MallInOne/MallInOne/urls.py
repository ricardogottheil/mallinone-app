from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin

from mall.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^api/local/', include('local.api.urls', namespace="api-local")),
    url(r'^api/mall/', include('mall.api.urls', namespace="api-mall")),
    url(r'^api/product/', include('product.api.urls', namespace="api-product")),
]