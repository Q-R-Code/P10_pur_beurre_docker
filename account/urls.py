from django.conf.urls import url
from django.urls import include

from . import views

app_name = 'account'

urlpatterns = [
    url(r'^inscription/', views.register, name='register'),
    url(r'^connection/', include("django.contrib.auth.urls"))
]
