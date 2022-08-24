from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializers
# from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
# from rest_framework.filters import OrderingFilter
class StudentList(ListAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['city']
    filter_backends = [SearchFilter]
    search_fields = ['name'] 
    # filter_backends = [OrderingFilter]
    # ordering_fields = ['name']