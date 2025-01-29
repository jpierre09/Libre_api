from rest_framework import serializers
from .models import Templates, Content

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Templates
        fields = '__all__'  




class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'  
