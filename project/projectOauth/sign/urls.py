from django.urls import re_path
from sign import views

urlpatterns = [
    re_path(r'^$', views.SignUp.as_view(), name="sign_up"),
]