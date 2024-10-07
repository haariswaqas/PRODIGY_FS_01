from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView
from api.models import User, Profile, Note
from api.serializers import UserSerializer, ProfileSerializer, MyTokenObtainPairSerializer, RegisterSerializer, NoteSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class ProfileView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)  # Just reuse the same logic as PUT

    def perform_update(self, serializer):
        serializer.save()



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk, user=request.user)
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    elif request.method == 'PUT':
        request.data['user'] = request.user.id
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def note_list(request):
    if request.method == 'GET':
        notes = Note.objects.filter(user=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # Associate the authenticated user with the note
        request.data['user'] = request.user.id
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)
    elif request.method == 'PUT':
        request.data['user'] = request.user.id
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









        
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lecturer_list(request):
    if request.method == 'GET':
        lecturers = Lecturer.objects.filter(user=request.user)
        serializer = LecturerSerializer(lecturers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        request.data['user'] = request.user.id
        serializer = LecturerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def lecturer_list(request):
#     if request.method == 'GET':
#         lecturers = Lecturer.objects.filter(user=request.user)
#         serializer = LecturerSerializer(lecturers, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         # Create a mutable copy of request.data
#         mutable_data = request.data.copy()
#         # Assign the user ID to the mutable copy
#         mutable_data['user'] = request.user.id
#         serializer = ProfileSerializer(data=mutable_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def lecturer_detail(request, pk):
    lecturer = get_object_or_404(Lecturer, pk=pk, user=request.user)
    if request.method == 'GET':
        serializer = LecturerSerializer(lecturer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        request.data['user'] = request.user.id
        serializer = LecturerSerializer(lecturer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        lecturer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.filter(user=request.user)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        request.data['user'] = request.user.id
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk, user=request.user)
    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    elif request.method == 'PUT':
        request.data['user'] = request.user.id
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






        