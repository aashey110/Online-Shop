from django.urls import path
from . import views


urlpatterns = [
    path('contact_store/', views.contact_store, name = "contact_store"),
    path('contact_valiadtion/', views.contact_validation, name = "contact_validation"),
]