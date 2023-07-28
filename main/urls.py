from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registration_view, name='registration_view'),
    path('login/', views.login_view, name='login_view'),
    path('login_sucess', views.login_success, name='login_success'),
    path('registration_successful', views.registration_successful, name='registration_successful')
]
