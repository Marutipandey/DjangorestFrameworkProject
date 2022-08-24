from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializers
# Create your views here.
class StudentList(ListAPIView):
    # queryset = Student.objects.filter(passby='admin1')
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)