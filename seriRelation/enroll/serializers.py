from dataclasses import fields
from . models import Song,Singer
from  rest_framework import serializers
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']

class SingerSerializer(serializers.ModelSerializer):
    songby = SongSerializer(many = True,read_only = True)
    # song = serializers.StringRelatedField(many = True, read_only = True)
    # song = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    # song = serializers.HyperlinkedRelatedField(many = True, read_only = True,view_name = 'song-detail')
    # song = serializers.SlugRelatedField(many = True, read_only = True,slug_field='title')
    # song = serializers.HyperlinkedIdentityField(view_name= 'song-detail')
    class Meta:
        model = Singer
        fields = ['id','name','gender','song','songby'] #song means jo related name model me hoga vahi likha jayega