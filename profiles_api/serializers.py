from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    '''Serializing some fields for testing APIView'''
    username = serializers.CharField(max_length=20)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
