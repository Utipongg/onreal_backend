from rest_framework import serializers
from .models import Course, Lesson, Enrollment
from djoser.serializers import UserSerializer as BaseUserSerializer

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__' 


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'instructor_name', 'instructor_image', 'category', 'cover_image', 'created_at','updated_at', 'lessons']



class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__' 


class UserSerializer(BaseUserSerializer):
    enrollments = serializers.SerializerMethodField()

    class Meta(BaseUserSerializer.Meta):
        fields = BaseUserSerializer.Meta.fields + ('enrollments',)

    def get_enrollments(self, obj):
        enrollments = Enrollment.objects.filter(student=obj)  # Use 'student' instead of 'user'
        return CourseSerializer([enrollment.course for enrollment in enrollments], many=True).data
