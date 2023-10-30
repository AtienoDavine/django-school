from django.urls import path
from students import views

app_name = "students"
urlpatterns = [

    path('', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('classes/', views.classes, name='classes'),
    path('add/', views.add, name='add'),
]
