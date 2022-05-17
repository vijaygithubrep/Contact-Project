from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.ContactList.as_view()),
    path('contact/<int:pk>/', views.ContactDetail.as_view()),
    path('company/', views.CompanyList.as_view()),
    path('company/<int:pk>/', views.CompanyDetail.as_view()),
    ]
