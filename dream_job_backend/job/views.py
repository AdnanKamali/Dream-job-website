from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Job, Category
from .serializers import JobSerializer, JobDetailSerializer, CategorySerializer
from .forms import JobForm


class CategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


class MyJobsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        my_jobs = Job.objects.filter(created_by=request.user)
        serializer = JobSerializer(my_jobs, many=True)
        return Response(serializer.data)


class CreateJobView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        form = JobForm(request.data)

        if form.is_valid():

            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return Response({"status": "created"})

        return Response({"status": "errors", "errors": form.errors})

    def put(self, request, pk):
        job = Job.objects.filter(created_by=request.user, pk=pk).first()

        form = JobForm(instance=job, data=request.data)
        if form.is_valid():
            job = form.save()

            return Response({"status": "updated"})

        return Response({"status": "errors", "errors": form.errors})

    def delete(self, request, pk):
        job = Job.objects.filter(created_by=request.user, pk=pk)

        job.delete()
        return Response({"status": "deleted"})


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


class BrowseJobsView(APIView):
    def get(self, request):
        jobs = Job.objects.all()

        query = request.GET.get("query", "")

        if query:
            jobs = jobs.filter(title__icontains=query)

        categories = request.GET.get("categories", "")

        if categories:
            jobs = jobs.filter(category_id__in=categories.split(","))

        serializer = JobSerializer(jobs, many=True)

        return Response(serializer.data)
