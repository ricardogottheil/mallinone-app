from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin

from mall.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index)
]