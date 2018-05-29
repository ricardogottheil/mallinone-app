
from django.conf.urls import url, include

from .views import LocalRudView, LocalAPIView

urlpatterns = [
    url(r'^$', LocalAPIView.as_view(), name='local-create'),
    url(r'^(?P<pk>\d+)/$', LocalRudView.as_view(), name='local-rud')
]