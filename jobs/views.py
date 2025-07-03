from django.shortcuts import render
from rest_framework import generics, permissions,exceptions
from .models import Job
from .serializer import JobSerializer


# Create your views here.

# List all jobs or create a new job
class JobListView (generics.ListAPIView):
    # queryset= Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        return Job.objects.filter(is_active=True)
class JobListCreateView(generics.CreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the employer
        serializer.save(employer_id = self.request.user.id)
    
class JobDetailView(generics.RetrieveAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]  # Open access to everyone
    
    def get_object(self):
        try:
            job = Job.objects.get(id=self.kwargs['job_id'],is_active=True)
        except Exception as e:
            raise exceptions.NotFound('Active job not found with this id')
        return job
        
    
    