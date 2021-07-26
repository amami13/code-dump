from .models import *
from rest_framework import serializers


class FileVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileVersion
        fields = ['created']

class FileSerializer(serializers.ModelSerializer):
    file_versions = FileVersionSerializer(many=True)

    def create(self, validated_data):
        
        file_versions = validated_data.pop('file_versions')
        
        file = File.objects.create(**validated_data)
        
        file_text = File
        for file_version in file_versions:
            FileVersion.objects.create(file=file, **file_version)
        return file

    class Meta:
        model = File
        fields = ['uuid', 'name', 'user', 'upvote', 'downvote']
        


