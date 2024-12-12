
from django.urls import path
from . import views
app_name='usd'
urlpatterns = [
    path('', views.usd, name='usd'),
    
] 

