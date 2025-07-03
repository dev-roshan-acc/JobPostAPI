from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.exceptions import (NotAuthenticated,NotFound,PermissionDenied,ValidationError) 
from django.core.exceptions import PermissionDenied as DjangoPermissionDenied


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, NotAuthenticated):
            code = "not_authenticated"
            status_code = status.HTTP_401_UNAUTHORIZED
        elif isinstance(exc, (PermissionDenied,DjangoPermissionDenied)):
            code = "permission_denied"
            status_code = status.HTTP_403_FORBIDDEN
        elif isinstance(exc, NotFound):
            code = "not_found"
            status_code = status.HTTP_404_NOT_FOUND
        elif isinstance(exc, ValidationError):
            code = "validation_error"
            status_code = status.HTTP_400_BAD_REQUEST
        else:
            code = f"error {isinstance(exc, PermissionDenied)}"
            status_code = response.status_code

        response.data = {
            "success": False,
            "error": {
                "code": code,
                "message": response.data.get("detail", str(exc)),
            },
        }
        response.status_code = status_code
        return response

    # Fallback for unhandled exceptions
    return Response(
        {
            "success": False,
            "error": {
                "code": "error",
                "message": "An unexpected error occurred.",
            },
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )

class BaseListAPIView(ListAPIView):

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return Response(
                {
                    "success": True,
                    "data": serializer.data,
                    "total": len(serializer.data),
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return custom_exception_handler(e, {"request": request})


class BaseCreateAPIView(CreateAPIView):
    def create(self, request, *args, **kwargs):
        try:

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            return custom_exception_handler(e, {"request": request})


class BaseUpdateAPIView(UpdateAPIView):

    def patch(self, request, *args, **kwargs):
        try:
            return self.partial_update(request, *args, **kwargs)

        except Exception as e:
            return custom_exception_handler(e, {"request": request})

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            partial = request.method = "PATCH" or kwargs.pop("partial", False)
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial
            )
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(
                {"success": True, "data": serializer.data}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return custom_exception_handler(e, {"request": request})
