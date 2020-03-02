from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),

    # registration
    path('register', views.register, name='register'),
    path('register/<slug>', views.register, name='register'),
]