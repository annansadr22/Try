from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('faq/', views.faq ,name='faq'),
    path('contact-us/', views.contact_us ,name='contact-us'),
    path('form-job/', views.form_job ,name='form-job'),
    path('form-freelance/', views.form_freelance ,name='form-freelance'),
    
]