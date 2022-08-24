from functools import partial
from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from enroll.models import Student
from enroll.serializers import StudentSerializer
from rest_framework import status
# Create your views here.
from rest_framework.views import APIView

# @api_view(['GET','POST','PUT','PATCH','DELETE'])
class student_api(APIView):
    def get(self,request,pk=None,format=None):
        if request.method=='GET':
            # id=request.data.get('id')
            id=pk
            if id is not None:
                stu=Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            stu=Student.objects.all()
            serializer = StudentSerializer(stu,many=True)
            return Response(serializer.data)
    
    def post(self,request,format=None):
        if request.method == 'POST':
            serializer=StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'data created !!'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
    
    def put(self,request,pk=None,format=None):
        if request.method =='PUT':
            # id=request.data.get('id')
            id=pk
            stu=Student.objects.get(pk=id)
            serializer=StudentSerializer(stu,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'data updated'})
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None,format=None):
        if request.method=="DELETE":
            # id=request.data.get('id')
            id=pk
            stu=Student.objects.get(pk=id)
            stu.delete()
            return Response({'msg':'data deleted'})  

