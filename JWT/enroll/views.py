from enroll.models import Student
from .serializers import StudentSerializer
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.authentication import SessionAuthentication
from enroll.customauth import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny,IsAuthenticatedOrReadOnly
from rest_framework import viewsets
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classess = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
   
