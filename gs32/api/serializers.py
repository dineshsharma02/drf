from rest_framework import serializers
from .models import Singer,Song

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['id','url','title','singer','duration']

class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True,read_only=True) #for string data sending
    # song = serializers.PrimaryKeyRelatedField(many=True,read_only=True) # for pk data sending
    # song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail') # for hyperlinked data sending
    # song = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title') # shows provided slug field data
    song = serializers.HyperlinkedIdentityField(many=True,read_only=True,view_name='song-detail')  # for hyperlinked data sending
    
    class Meta:
        model = Singer
        fields = ['id','name','gender','song'] ## this 'song' is reffered from related_name in models if not defined in this class