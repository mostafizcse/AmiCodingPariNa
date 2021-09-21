from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'myApp'
#router = routers.DefaultRouter()
#router.register('heroes', views.DataViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.getLogin, name="login"),
    path('signIn', views.getRegister, name="signIn"),
    path('api', views.dataViewSet, name="api"),
]
