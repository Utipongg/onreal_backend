from rest_framework import serializers
from rest_framework.response import responses
from rest_framework import status
from .models import ImageModel

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'

    def to_representation(self, instance):
            representation = super().to_representation(instance)
            request = self.context.get('request')
            if request:
                representation['image'] = request.build_absolute_uri(instance.image.url)
            return representation