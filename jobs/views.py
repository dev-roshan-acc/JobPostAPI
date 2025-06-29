from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Job
from .serializer import JobSerializer

# Create your views here.

# List all jobs or create a new job
class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the employer
        serializer.save(employer_id = self.request.user.id)
    
class JobDetailView(generics.RetrieveAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]  # Open access to everyone
    
    def get_object(self):
        id = self.kwargs['job_id']
        return Job.objects.get(id=id)
        
    
    