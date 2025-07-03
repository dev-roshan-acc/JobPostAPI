from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.response import Response
from rest_framework import status
class BaseListAPIView (ListAPIView):
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset,many=True)
            return Response({
                "success":True,
                "data":serializer.data,
                "total":len(serializer.data)
            },status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "success":False,
                "data":str(e),
                "total":0
            },status=status.HTTP_400_BAD_REQUEST)
    
class BaseCreateAPIView (CreateAPIView):
    def create(self, request, *args, **kwargs):
        try:
            
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({
                "success":True,
                "data":serializer.data
            },status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({
                "success":False,
                "data":str(e)
            },status=status.HTTP_400_BAD_REQUEST)
    