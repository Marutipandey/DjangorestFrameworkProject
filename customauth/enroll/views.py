from enroll.models import Student
from .serializers import StudentSerializer
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.authentication import SessionAuthentication
from enroll.customauth import CustomAuthentication

from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
from rest_framework import viewsets
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classess = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
   
