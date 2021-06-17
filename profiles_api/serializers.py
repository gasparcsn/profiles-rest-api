from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    '''Serializing some fields for testing APIView'''
    username = serializers.CharField(max_length=20)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)


class UserProfileSerializer(serializers.ModelSerializer):
    '''Serializes a user profile object'''

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{
                    'input_type':'password'
                }
            }
        }

    def create(self, validated_data):
        '''Create and return new user'''

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )

        return user

    def update(self, instance, validated_data):
        '''Handle updating user account'''

        if 'password' in validated_data:
            password = validated_data.pop['password']
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    '''Serializes profile feed items'''

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}
