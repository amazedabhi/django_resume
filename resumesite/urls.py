from django.urls import path
from resumesite import views

urlpatterns = [
    path('', views.index)
]