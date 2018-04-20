from rest_framework import serializers

from Api.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = '__all__'