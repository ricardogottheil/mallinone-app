from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^mall/$', MallList.as_view(), name='mall'),
]