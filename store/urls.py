

from django.urls import path, include

from store import views

urlpatterns = [
    path('', views.redirect, name='index'),
    path('documents/', views.documents, name='documents'),
    path('new_document/', views.new_document, name='new_document'),
    path('update_document/', views.update_document, name='update_document'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    path('api/documents/', views.api_documents, name='api_documents'),
    path('api/document/<int:document_id>/', views.api_document, name='api_document'),
    path('api/chip/', views.api_chip, name='api_chip'),
]
