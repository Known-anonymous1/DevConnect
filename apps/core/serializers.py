#Serialzers for the Project model
# This file is part of the Project Management System.

from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'owner', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']
        
#Serializers for Transaction model

from .models import Transaction  # Add if not already imported

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'project', 'amount', 'description', 'type', 'created_at']
        read_only_fields = ['id', 'created_at']
    