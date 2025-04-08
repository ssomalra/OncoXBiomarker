from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage with buttons
    path('cancer-type/<str:cancer_name>/', views.cancer_type_page, name='cancer_type_page'),  # Name-based page for image buttons
    path('subtype/<str:subtype_name>/', views.subtype_detail, name='subtype_detail'),  # Subtype-specific view
    path('biomarker/<str:biomarker_id>/', views.biomarker_detail, name='biomarker_detail'),  # Biomarker detail page
    path('help/', views.help_page, name='help_page')  # Help page
]