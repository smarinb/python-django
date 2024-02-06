
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello, name='hello'),
    path('bie/', views.bie, name = 'bie'),
    path('adult/<int:age>/',views.adult, name='adult')
]
