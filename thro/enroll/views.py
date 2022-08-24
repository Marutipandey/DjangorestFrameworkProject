from enroll.models import Student
from .serializers import StudentSerializer
# from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication
# from enroll.customauth import CustomAuthentication

from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny,IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from enroll.throttling import JackRateThrottle
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classess = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
   
