from django.urls import path

from . import views

urlpatterns = [
    path("newest/", views.NewestJobsView.as_view()),
    path("<int:pk>/", views.JobDetailView.as_view()),
]
