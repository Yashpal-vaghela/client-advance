
from django.urls import path
from . import views
app_name='enquiry'
urlpatterns = [
    path('newsletter/', views.newsletter, name='newsletter'),
    path('review/', views.review, name='review'),
    path('contact-data/', views.contactd, name='contactd'),
    
] 
