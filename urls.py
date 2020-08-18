from django.conf.urls import url
from app_header import views

urlpatterns = [
    url('', views.index, name="index"),
]
