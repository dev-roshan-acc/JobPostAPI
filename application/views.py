from rest_framework import generics,permissions
from .serializer import ApplicationSerializer
from jobs.models import Job
from django.shortcuts import get_object_or_404
from .models import Application
from rest_framework.response import Response
from core.base_views import BaseListAPIView,BaseCreateAPIView,BaseUpdateAPIView
from core.master_utils import MasterApplicationUtils
# Create your views here.


class ApplyToJobView(BaseCreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        job_id = self.kwargs.get('job_id')
        context['job'] = get_object_or_404(Job,pk=job_id)
        context['user'] = self.request.user
        
        return context
    def perform_create(self, serializer):
        serializer.save()


class UserApplicationView(BaseListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)
    
class ApplicationListView(BaseListAPIView):
    serializer_class=ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        # In the code snippet
        # provided, the `__`
        # (double underscore) is
        # used in Django's ORM
        # (Object-Relational
        # Mapping) to perform a
        # lookup that spans
        # relationships.
        
        return Application.objects.filter(job__employer=self.request.user)
    
class WithdrawApplicationView (BaseUpdateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Application.objects.all()
    lookup_url_kwarg = 'application_id'
    
    # def get_queryset(self):
        # return Application.objects.filter(user=self.request.user,status = 'applied')
        
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
    
    def patch(self, request, *args, **kwargs):
        application_id =self.kwargs.get(self.lookup_url_kwarg)
        MasterApplicationUtils.update_application_status(application_id,self.request.user,'withdraw')
        # application = self.get_object()
        # application.status = 'withdrawn'
        # application.save()
        return super().patch(request, *args, **kwargs)
        
        