
from django.conf.urls import url, include

from .views import MallRudView, MallAPIView

urlpatterns = [
    url(r'^$', MallAPIView.as_view(), name='mall-create'),
    url(r'^(?P<pk>\d+)/$', MallRudView.as_view(), name='mall-rud')
]