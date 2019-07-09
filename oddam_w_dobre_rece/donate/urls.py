from django.conf.urls import url
from donate.views import index

urlpatterns = [
    url('', index, name='index'),
]
