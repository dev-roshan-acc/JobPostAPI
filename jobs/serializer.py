from rest_framework import serializers
from locations.serializer import LocationSerializer
from .models import Job
from locations.models import Location


class JobSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'salary', 'location', 'employer_id', 'created_at', 'is_active']
        read_only_fields = ["employer_id", "created_at"]

    def create(self, validated_data):
        location_data = validated_data.pop("location")
        print("location_data type:", type(location_data))  # Should be dict
        print("location_data content:", location_data)
        location = Location.objects.create(**location_data)
        print("Created location:", location)
        job = Job.objects.create(location=location)
        print("Created job:", job)
        return job
