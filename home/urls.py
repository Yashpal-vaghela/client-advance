
from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('', views.api_user_login, name='api_user_login'),
    
    path('client-profile/<str:pk>/<str:fk>/', views.ext_api, name='ext_api'),
    path('print-order/', views.print_order, name='print_order'),
    path('print-payment/', views.print_payment, name='print_payment'),
    path('print-statments/<str:pk>/<str:did>/', views.print_statment, name='print_statment'),
    path('print-invoice/<str:pk>/<str:did>/', views.print_invoice, name='print_invoice'),
    path('api-logout/<str:pk>/<str:did>/', views.api_logout, name='api_logout'),
    

] 

