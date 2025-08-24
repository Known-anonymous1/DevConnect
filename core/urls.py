#URLs for the Project app
# This file is part of the Project Management System.

from django.urls import path
from .views import ProjectListCreateView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create')
]


#URLs for Transaction model

from .views import ProjectListCreateView, TransactionListCreateView

urlpatterns = [
    path('projects/', TransactionListCreateView.as_view(), name='project-list-create'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
]

from django.urls import path
from .views import (
    ProjectListCreateView, ProjectRetrieveUpdateDestroyView,
    TransactionListCreateView, TransactionRetrieveUpdateDestroyView
)

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    