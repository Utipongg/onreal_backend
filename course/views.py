from django.shortcuts import render
from rest_framework import generics
from .models import Course, Lesson, Enrollment
from .serializers import CourseSerializer, LessonSerializer, UserSerializer,EnrollmentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny 


# Create your views here.


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get_permissions(self):
                if self.request.method == 'GET':
                    return [AllowAny()]
                elif self.request.method == 'POST':
                    return [IsAuthenticated()]
                return super().get_permissions()


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get_permissions(self):
            if self.request.method == 'GET':
                return [AllowAny()]
            elif self.request.method == 'PUT' or self.request.method == "DELETE":
                return [IsAuthenticated()]
            return super().get_permissions()
    
# -----------------------------------
class LessonList(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    def get_permissions(self):
                if self.request.method == 'GET':
                    return [AllowAny()]
                elif self.request.method == 'POST':
                    return [IsAuthenticated()]
                return super().get_permissions()


class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    def get_permissions(self):
            if self.request.method == 'GET':
                return [AllowAny()]
            elif self.request.method == 'PUT' or self.request.method == "DELETE":
                return [IsAuthenticated()]
            return super().get_permissions()
    
# -----------------------------------
class EnrollmentList(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    def get_permissions(self):
                if self.request.method == 'GET':
                    return [AllowAny()]
                elif self.request.method == 'POST':
                    return [IsAuthenticated()]
                return super().get_permissions()


class EnrollmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    def get_permissions(self):
            if self.request.method == 'GET':
                return [AllowAny()]
            elif self.request.method == 'PUT' or self.request.method == "DELETE":
                return [IsAuthenticated()]
            return super().get_permissions()