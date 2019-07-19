from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.ind, name='index'),
    path('components/', views.components_list, name='components_list'),
    path('components/new/', views.components_new, name='components_new'),
    path('comp/', views.comp, name='comp'),
    path('login/', LoginView.as_view(template_name='app74/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]