# ENTRY POINT for all the urls in the app
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


routers = DefaultRouter()
#first arg: name of the URL that we want to create
#second arg: the viewset
# third: base name
routers.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')


urlpatterns = [
    # we map the end point hello-view to the class HelloApiView
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(routers.urls))
]
