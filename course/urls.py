from django.urls import path
from .views import CourseList, CourseDetail, LessonList, LessonDetail, EnrollmentList, EnrollmentDetail

urlpatterns = [
    path('courselist/', CourseList.as_view()),
    path("courselist/<int:pk>/", CourseDetail.as_view()),
    path('lessonlist/', LessonList.as_view()),
    path("lessonlist/<int:pk>/", LessonDetail.as_view()),
    path('enrollmentlist/', EnrollmentList.as_view()),
    path("enrollmentlist/<int:pk>/", EnrollmentDetail.as_view()),
]