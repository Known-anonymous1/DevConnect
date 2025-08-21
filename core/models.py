from django.contrib.auth.models import AbstractUser
from django.db import models

#Custom user model
class User(AbstractUser):
    # You can add additional fields here if needed
    pass

#Project model to hold project details
class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
#Transaction model to track financial /resouces transactions within a project
class Transaction(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    RESOURCE = 'resource'
    FINANCE = 'finance'
    TYPE_CHOICES = [
        (RESOURCE, 'Resource'),
        (FINANCE, 'finance'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=FINANCE)

    def __str__(self):
        return f"{self.type} | {self.description} | {self.amount}"
    
                                   