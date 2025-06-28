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
        fields = ["username", "email", "password", "is_employer", "is_job_seeker"]
