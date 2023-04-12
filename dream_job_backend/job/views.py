from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Job, Category
from .serializers import JobSerializer, JobDetailSerializer, CategorySerializer


class CategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


class NewestJobsView(APIView):
    def get(self, request):
        jobs = Job.objects.all()[0:4]
        serializer = JobSerializer(jobs, many=True)

        return Response(serializer.data)


class JobDetailView(APIView):
    def get(self, request, pk):
        job = Job.objects.get(pk=pk)
        serializer = JobDetailSerializer(job)

        return Response(serializer.data)
