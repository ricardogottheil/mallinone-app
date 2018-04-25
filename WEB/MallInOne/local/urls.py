from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^local/$', LocalList.as_view(), name='local'),
]