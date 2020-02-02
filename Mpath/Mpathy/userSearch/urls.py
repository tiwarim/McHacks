from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('api/users', views.UserListCreate.as_view()),
    url(r'^api/$', views.ListMatchedTwitterID.as_view())
]
