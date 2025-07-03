from django.urls import path
from .views import JobListCreateView,JobDetailView,JobListView



urlpatterns = [
    path('', JobListView.as_view(), name='job-list'),
    path('create/', JobListCreateView.as_view(), name='job-list'),
    
    path('<int:job_id>/', JobDetailView.as_view(), name='job-details')
    
]
