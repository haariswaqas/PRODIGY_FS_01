from api.models import User, Profile, Note, Lecturer, Course

from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token['username'] = user.username
        token['email'] = user.email

        token['first_name'] = user.profile.first_name
        token['middle_name'] = user.profile.middle_name
        token['last_name'] = user.profile.last_name
        token['bio'] = user.profile.bio
        token['image'] = str(user.profile.image)
        token['verified'] = user.profile.verified

        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    password2 = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields do not match"}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Profile
        fields = '__all__'


class LecturerSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Lecturer
        fields = ['id', 'user', 'title', 'first_name', 'middle_name', 'last_name', 'bio']
        read_only_fields = ['id']


class CourseSerializer(serializers.ModelSerializer):
    lecturer_title = serializers.CharField(source='lecturer.title', read_only=True)
    lecturer_first_name = serializers.CharField(source='lecturer.first_name', read_only=True)
    lecturer_middle_name = serializers.CharField(source='lecturer.middle_name', read_only=True)
    lecturer_last_name = serializers.CharField(source='lecturer.last_name', read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['id']




class NoteSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Note
        fields = ['id', 'user', 'title', 'content', 'created', 'updated']
        read_only_fields = ['id', 'created', 'updated']

