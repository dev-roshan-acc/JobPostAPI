from django.urls import path
from .views import ApplyToJobView,UserApplicationView,ApplicationListView,WithdrawApplicationView

urlpatterns = [
    path('apply/<int:job_id>/',ApplyToJobView.as_view(),name='apply_job'),
    path('my-application/',UserApplicationView.as_view(),name='my-application-list'),
    path('list/',ApplicationListView.as_view(),name='list'),
    path('<int:application_id>/withdraw/',WithdrawApplicationView.as_view(),name='withdraw-application')
]
