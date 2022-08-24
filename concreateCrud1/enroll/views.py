from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Student
from.serializers import StudentSerializer

class LCStudentApi(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class RUDStudentRetrive(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    