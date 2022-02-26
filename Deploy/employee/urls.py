from django.conf.urls import url
from employee import views

urlpatterns = [
    url('digit', views.digit, name='digit'),
]
