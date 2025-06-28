from rest_framework import serializers
from locations.serializer import LocationSerializer
from .models import Job
from locations.models import Location
from django.db import transaction


class JobSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()
    
    def get_location(self,obj):
        return f"{obj.location.city},{obj.location.state},{obj.location.postcode},{obj.location.country}"
    employer_username = serializers.CharField(source='employer.username', read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'salary', 'location', 'employer_username', 'created_at', 'is_active']
        read_only_fields = ["employer_id", "created_at"]

    def create(self, validated_data):
        location_data = validated_data.pop("location")
        with transaction.atomic():
            location = Location.objects.create(**location_data)
            job= Job.objects.create(location=location, **validated_data)
            return job

