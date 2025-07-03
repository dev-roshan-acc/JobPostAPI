from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=_("A user with that email already exists.")
            )
        ]
    )
    password = serializers.CharField(write_only=True,validators=[validate_password])

    class Meta:
        model = User
        fields = ["username", "email", "password", "is_employer", "is_job_seeker","first_name","last_name"]
    
    def create(self,validated_data):
        user = User(
        username=validated_data['username'],
        email=validated_data['email'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        is_employer=validated_data['is_employer'],
        is_job_seeker=validated_data['is_job_seeker'],
        )
        user.set_password(validated_data['password'])  # hashes password
        user.save()
        return user
