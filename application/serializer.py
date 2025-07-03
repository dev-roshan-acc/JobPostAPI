
from rest_framework import serializers
from .models import Application
class ApplicationSerializer(serializers.ModelSerializer):
    job = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=Application
        fields=['id', 'job', 'user', 'resume', 'cover_letter', 'status', 'applied_at']
        read_only_fields = ['status', 'applied_at']
    
    def validate(self, attrs):
        user = self.context['request'].user
        job = attrs.get('job')
        if Application.objects.filter(user=user,job=job).exists():
            raise serializers.ValidationError('You have already applied for this job.')
        return attrs
    
    def create(self, validated_data):
        user = self.context['user']
        job = self.context['job']
        return Application.objects.create(user=user,job=job,**validated_data)