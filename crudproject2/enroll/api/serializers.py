from dataclasses import fields
from enroll.models import User
from rest_framework import serializers
class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','password']