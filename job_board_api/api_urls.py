from django.urls import path, include

urlpatterns = [
    path("account/", include("accounts.urls")),
    path("jobs/", include("jobs.urls")),
    path("application/", include("application.urls")),
    
]
