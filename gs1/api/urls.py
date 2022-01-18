
from django import views
from django.urls import  path
from . import views

urlpatterns = [
    path('api/student/<int:pk>',views.student_detail),
    path('api/student/all',views.student_list),
]