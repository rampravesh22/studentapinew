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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # Validate the data
        serializer.is_valid(raise_exception=True)

        # Save the object to the database
        self.perform_create(serializer)

        return Response({"msg": "created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Add your custom logic here before calling the base destroy method,
        # if needed. For example, you can check permissions, log actions, etc.

        # Call the base destroy method to delete the instance.
        self.perform_destroy(instance)

        # Return a custom response indicating successful deletion.
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
