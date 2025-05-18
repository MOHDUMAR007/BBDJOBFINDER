"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import browse, resumeDetail, company_login, company_dashboard
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("browse/", browse, name="browse"),
    path("view-detail/<int:resume_id>/", resumeDetail, name="resumeDetail"),
    path('company_login/', company_login, name='company_login'),
    path('company_dashboard/', company_dashboard, name='company_dashboard'),
    path('company_register/', views.company_register, name='company_register'),
    path('company_login/', views.company_login, name='company_login'),
    path('company_dashboard/', views.company_dashboard, name='company_dashboard'),
    path('company_logout/', views.company_logout, name='company_logout'),
    path('resume_status/', views.resume_status, name='resume_status'),
    path('upload_resume/', views.upload_resume, name='upload_resume'),
    path('delete_resume/<int:resume_id>/', views.delete_resume, name='delete_resume'),
    path('submit/', views.submit_resume, name='submit_resume'),
    path('company_profile/', views.manage_company_profile, name='manage_company_profile'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')),
    path('help/', TemplateView.as_view(template_name="help.html"), name="help"),
    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
    path('contact/', TemplateView.as_view(template_name="contact.html"), name="contact"),
    path('terms/', TemplateView.as_view(template_name="Terms.html"), name="terms"),
    path('privacy/', TemplateView.as_view(template_name="privacy.html"), name="privacy"),
    path('reference/<int:ref_id>/update/', views.update_reference_status, name='update_reference_status'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
