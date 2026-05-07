from django.urls import path
from .views import (
    RegisterView,
    ProjectListCreateView,
    ProjectRetrieveUpdateDestroyView,
    TransactionListCreateView,
    TransactionRetrieveUpdateDestroyView,
    ProjectExportView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/export/', ProjectExportView.as_view(), name='project-export'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateDestroyView.as_view(), name='transaction-detail'),
]
