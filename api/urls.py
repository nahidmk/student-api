
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import StudentView,saveInfo,getInfo

from api import urls

router = DefaultRouter()

router.register('api',StudentView,basename='student')

urlpatterns = [
    path('',include(router.urls)),
    path('reg/',saveInfo.as_view()),
    path('info/',getInfo)

]