from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from mall.views import index

API_TITLE = 'MallinOne API'
API_DESCRIPTION = 'Web API by MallinOne'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^api/v1/auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include('local.urls', namespace='local')),
    url(r'^api/v1/', include('mall.urls', namespace='mall')),
    url(r'^api/v1/', include('product.urls', namespace='product')),
    url(r'^schema/$', schema_view)
    #url(r'^docs/', include_docs_urls(title='MallinOne API', description='Web API by MallinOne'))
]