from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor_name = models.CharField(max_length=255)  # Changed from ForeignKey to CharField
    instructor_image = models.ImageField(upload_to='instructor_images/', null=True, blank=True)  # Image for instructor
    category = models.CharField(max_length=100, blank=True)
    cover_image = models.ImageField(upload_to='course_covers/', null=True, blank=True)  # Image cover field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    content = models.TextField()  # Could include text or HTML content
    video_url = models.URLField(blank=True, null=True)  # For video lessons
    order = models.PositiveIntegerField(default=0)  # Lesson order within the course
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f'{self.student.username} enrolled in {self.course.title}'
