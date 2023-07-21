from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.models import Student
from rest_framework import status
from rest_framework.response import Response
from core.serializers import StudentSerializer
# Create your views here.


class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def destroy(self, request, *args, **kwargs):
        student = self.get_object()
        self.perform_destroy(instance=student)
        return Response({"msg": f"student with name {student.name} delete successfully"}, status=status.HTTP_204_NO_CONTENT)
