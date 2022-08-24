from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# -----GET-------------
"""
@api_view()
def hello_world(request):
    return Response({'msg':'Hello world'})"""


# -------POST------------
"""
@api_view(['POST'])
def hello_world(request):
    if request.method == "POST":
        print(request.data)
        return Response({'res':'this is a post request'})
        """


# ------- GET/POST BOTH ------------

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == "GET":
        print(request.data)
        return Response({'res':'this is a GET request'})
    if request.method == "POST":
        print(request.data)
        return Response({'res':'this is a post request','data':request.data})
       
