

from django.urls import path, include

from store import views

urlpatterns = [
    path('', views.redirect, name='index'),
    path('documents/', views.documents, name='documents'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    path('api/documents/', views.api_documents, name='api_documents'),
]
