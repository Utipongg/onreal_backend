from django.urls import path
from .views import ImageUploadView, GetImageApiView

urlpatterns = [
    path('uploadimg-slide/', ImageUploadView.as_view(), name='image-upload'),
    path("getimg-slide/", GetImageApiView.as_view()),
    path("deleteimg-slide/<int:pk>/", ImageUploadView.as_view()),
]