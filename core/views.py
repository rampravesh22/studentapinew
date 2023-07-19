from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.models import Student
from core.serializers import StudentSerializer
# Create your views here.


class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
