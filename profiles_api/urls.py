# ENTRY POINT for all the urls in the app
from django.urls import path

from profiles_api import views


urlpatterns = [
    # we map the end point hello-view to the class HelloApiView
    path('hello-view/', views.HelloApiView.as_view())
]
