from django.conf.urls import url
from thirdapp import views

urlpatterns = [
    url(r'^$', views.user, name='users'),
]