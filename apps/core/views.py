import csv
import json
from django.http import HttpResponse
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Project, Transaction
from .serializers import (
    ProjectSerializer,
    TransactionSerializer,
    RegisterSerializer,
)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {"message": f"Account created successfully. Welcome, {user.username}!"},
            status=status.HTTP_201_CREATED
        )


class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)


class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(project__owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save()


class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(project__owner=self.request.user)


class ProjectExportView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        projects = Project.objects.filter(owner=request.user)
        export_format = request.query_params.get('format', 'csv')

        if export_format == 'json':
            data = list(projects.values(
                'id', 'name', 'description', 'created_at', 'updated_at'
            ))
            response = HttpResponse(
                json.dumps(data, indent=4, default=str),
                content_type='application/json'
            )
            response['Content-Disposition'] = 'attachment; filename="projects.json"'
            return response

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="projects.csv"'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Name', 'Description', 'Created At', 'Updated At'])
        for project in projects:
            writer.writerow([
                project.id,
                project.name,
                project.description,
                project.created_at,
                project.updated_at
            ])
        return response
