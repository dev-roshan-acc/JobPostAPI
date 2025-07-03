from core.base_views import BaseCreateAPIView
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializer import RegisterSerializer
from rest_framework.permissions import IsAdminUser

User = get_user_model()

class RegisterView(BaseCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

@api_view(['GET'])
@permission_classes([IsAdminUser])
def allUsers(request):
    all_user = User.objects.all()
    serializer = RegisterSerializer(all_user, many=True)
    return Response(serializer.data)
